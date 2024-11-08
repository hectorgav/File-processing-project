"""
This module handles file operations for organizing and moving scanned documents and photos.

It provides functionality to:
1. Find destination folders based on job numbers and file types.
2. Move folders to their appropriate destinations, merging if necessary.
3. Process multiple folders with a progress bar.

The module is designed to work with a specific directory structure and naming convention
for job-related files and folders. It handles both regular sales orders and stock jobs,
accommodating different folder structures for each type.

Key functions:
- find_destination_folder: Determines the correct destination for a given job number and file type.
- move_folder: Moves or merges a folder to its destination.
- process_folders: Processes multiple folders, moving them to their correct locations.

This module is part of a larger file processing system and is typically called from a GUI
or command-line interface.
"""

try:
    import os
    import shutil
    import logging
    from tqdm import tqdm
    from datetime import datetime
    from typing import Optional, Union, LiteralString
    from config.settings import DESTINATION_BASE, year_range_limit

    def find_destination_folder(job_number: str, file_type: str) -> Optional[str | LiteralString]:
        """Find the corresponding destination folder based on the job number and file type."""
        if not job_number.startswith("110") and len(job_number) >= 6 and job_number[:2].isdigit():
            year = job_number[:2]
            potential_path = os.path.join(DESTINATION_BASE, f"Sales Orders 20{year}")
            subfolder = r"Scans\Drawings" if file_type == 'pdf' else "Pictures"

        elif job_number.startswith("110") and job_number.isdigit():
            current_year = datetime.now().year
            subfolder = "Scans" if file_type == 'pdf' else "Pictures"
            for year in range(current_year, current_year - year_range_limit, -1):
                potential_path = os.path.join(DESTINATION_BASE, f"Stock Jobs {year}")
                for root, dirs, _ in os.walk(potential_path):
                    for directory in dirs:
                        if directory.startswith(job_number):
                            return os.path.join(root, directory, subfolder)
            logging.warning(f"No matching folder found for Stock Job number: {job_number}")
            return None

        else:
            logging.error(f"Invalid job number format: {job_number}")
            return None

        for root, dirs, _ in os.walk(potential_path):
            for directory in dirs:
                if directory.startswith(job_number):
                    return os.path.join(root, directory, subfolder)

        logging.warning(f"No matching folder found for job number: {job_number}")
        return None


    def move_folder(source_folder: str, file_type: str) -> None:
        """Move the entire folder to the destination, merging if it already exists."""
        folder_name: str = os.path.basename(source_folder)

        if len(folder_name) >= 6 and folder_name[:6].isdigit():
            job_number: str = folder_name[:6]
        elif folder_name.startswith("110") and len(folder_name) > 6:
            job_number: str = folder_name[:7]
        else:
            logging.error(f"Invalid folder name format: {folder_name}")
            return

        destination_folder: Optional[Union[str, LiteralString]] = find_destination_folder(job_number, file_type)
        if not destination_folder:
            logging.error(f"Destination folder not found for {folder_name}")
            return

        final_destination: str = os.path.join(destination_folder, folder_name)

        try:
            if not os.path.exists(final_destination):
                shutil.move(source_folder, final_destination)
                logging.info(f"Moved folder: {source_folder} -> {final_destination}")
            else:
                logging.info(f"Destination folder already exists. Merging contents: {source_folder} -> {final_destination}")
                shutil.copytree(source_folder, final_destination, dirs_exist_ok=True)
                shutil.rmtree(source_folder)
        except FileNotFoundError as e:
            logging.error(f"File not found error while moving folder {source_folder}: {str(e)}")
        except PermissionError as e:
            logging.error(f"Permission error while moving folder {source_folder}: {str(e)}")
        except shutil.Error as e:
            logging.error(f"Shutil error while moving folder {source_folder}: {str(e)}")
        except Exception as e:
            logging.error(f"Unexpected error while moving folder {source_folder}: {str(e)}")


    def process_folders(source_path: str, file_type: str) -> Optional[bool]:
        """Process all folders in the source directory with a progress bar."""
        try:
            folders = [entry for entry in os.scandir(source_path) if entry.is_dir() and
                    (entry.name[:6].isdigit() or (entry.name.startswith("110") and len(entry.name) > 6))]

            if not folders:
                logging.warning(f"No matching folders found in {source_path}")
                return None

            with tqdm(total=len(folders), desc="Processing folders", unit="folder") as pbar:
                for entry in folders:
                    move_folder(entry.path, file_type)
                    pbar.update(1)

            return True  # Return True if processing completes successfully
        except Exception as e:
            logging.error(f"Error processing folders: {str(e)}")
            return False  # Return False if an error occurs
    
except FileNotFoundError as e:
    logging.error(f"File not found error during imports: {str(e)}")
except PermissionError as e:
    logging.error(f"Permission error during imports: {str(e)}")
except Exception as e:
    logging.error(f"Unexpected error during imports: {str(e)}")
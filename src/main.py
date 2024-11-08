# src/main.py
import sys
import logging
from tkinter import messagebox
import shutil
from logs.logging_config import setup_logging
from .utils import validate_directory_structure
from .gui import run_gui
from config.settings import PDF_SOURCE, PHOTO_SOURCE_BASE, DESTINATION_BASE

def main():
    """Main entry point for the file processing application."""
    setup_logging()  
    
    try:
        # Validate directory structure before proceeding
        if not validate_directory_structure(PDF_SOURCE, PHOTO_SOURCE_BASE, DESTINATION_BASE):
            messagebox.showerror("Error", "Directory structure validation failed. Check the log for details.")
            sys.exit(1)

        run_gui()  # Run the GUI for user interaction

        # Show completion message after GUI processing
        messagebox.showinfo("Complete", "File processing completed. Check the log file for details.")

    except FileNotFoundError as e:
        logging.error(f"File not found error: {str(e)}")
        messagebox.showerror("Error", f"File not found: {str(e)}")
    except PermissionError as e:
        logging.error(f"Permission error: {str(e)}")
        messagebox.showerror("Error", f"Permission denied: {str(e)}")
    except shutil.Error as e:
        logging.error(f"Shutil error: {str(e)}")
        messagebox.showerror("Error", f"Error moving files: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
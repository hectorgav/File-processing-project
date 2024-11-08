# src/utils.py
import os
import sys
from datetime import datetime
from tkinter import messagebox
from config.settings import year_range_limit  


def long_path(path: str) -> str:
    """Convert a given path to a long path format if on Windows."""
    if sys.platform == 'win32':
        return f'\\\\?\\{os.path.abspath(path)}'
    return os.path.abspath(path)


def validate_directory_structure(pdf_source: str, photo_source_base: str, destination_base: str) -> bool:
    """Validate the directory structure for processing files.

    Args:
        pdf_source (str): The path to the PDF source directory.
        photo_source_base (str): The path to the photo source directory.
        destination_base (str): The base path for destination directories.

    Returns:
        bool: True if all directories exist; False otherwise.
    """
    current_year = datetime.now().year
    # structure_valid = True

    # Validate sales orders and stock jobs directories for recent years
    for year in range(current_year, current_year - year_range_limit, -1):
        sales_order_path = long_path(os.path.join(destination_base, f"Sales Orders 20{str(year)[2:]}"))
        stock_jobs_path = long_path(os.path.join(destination_base, f"Stock Jobs {year}"))

        if not os.path.exists(sales_order_path):
            warning_msg = f"Sales Orders directory for year {year} does not exist: {sales_order_path}"
            messagebox.showwarning("Warning", warning_msg)
            # logging.warning(warning_msg)
            # structure_valid = False

        if not os.path.exists(stock_jobs_path):
            warning_msg = f"Stock Jobs directory for year {year} does not exist: {stock_jobs_path}"
            messagebox.showwarning("Warning", warning_msg)
            # logging.warning(warning_msg)
            # structure_valid = False

    # Validate source directories
    if not os.path.exists(pdf_source):
        error_msg = f"PDF source directory does not exist: {pdf_source}"
        messagebox.showerror("Error", error_msg)
        # logging.error(error_msg)
        return False

    if not os.path.exists(photo_source_base):
        error_msg = f"Photo source directory does not exist: {photo_source_base}"
        messagebox.showerror("Error", error_msg)
        # logging.error(error_msg)
        return False

    return True
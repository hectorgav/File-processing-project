# src/gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from .file_operations import process_folders
from config.settings import PDF_SOURCE, PHOTO_SOURCE_BASE


def run_gui():
    """Run the GUI for processing photos or scans."""
    root = tk.Tk()
    root.title("File Processing")
    root.geometry("300x150")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    label = ttk.Label(frame, text="Choose an option:")
    label.grid(row=0, column=0, columnspan=2, pady=10)

    def process_photos():
        """Process photo folders."""
        try:
            messagebox.showinfo("Processing", "Processing photos. Check the console and log file for progress.")
            result = process_folders(PHOTO_SOURCE_BASE, 'photo')
            if result is None:
                messagebox.showinfo("Info", "No matching folders found for photos.")
            elif result:
                messagebox.showinfo("Success", "Photo processing completed successfully.")
            else:
                messagebox.showerror("Error", "An error occurred while processing photos. Check the log for details.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred while processing photos: {str(e)}")

    def process_scans():
        """Process scan folders."""
        try:
            messagebox.showinfo("Processing", "Processing scans. Check the console and log file for progress.")
            result = process_folders(PDF_SOURCE, 'pdf')
            if result is None:
                messagebox.showinfo("Info", "No matching folders found for scans.")
            elif result:
                messagebox.showinfo("Success", "Scan processing completed successfully.")
            else:
                messagebox.showerror("Error", "An error occurred while processing scans. Check the log for details.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred while processing scans: {str(e)}")

    photo_button = ttk.Button(frame, text="Process Photos", command=process_photos)
    photo_button.grid(row=1, column=0, padx=5, pady=5)

    scan_button = ttk.Button(frame, text="Process Scans", command=process_scans)
    scan_button.grid(row=1, column=1, padx=5, pady=5)

    root.mainloop()

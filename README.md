# File Processing App

This application is designed to efficiently organize and move scanned documents and images from source directories to specific destination folders based on job numbers and file types. It provides a user-friendly graphical interface for initiating the processing of either photos or scans.

## Features

- Graphical User Interface (GUI) for easy operation
- Processes both scanned documents (PDFs) and photos
- Automatically determines destination folders based on job numbers
- Handles long file paths on Windows systems
- Merges folders if the destination already exists
- Provides progress bars for visual feedback during processing
- Comprehensive logging for tracking operations and troubleshooting

## Requirements

- Python 3.6 or later
- Required Python packages:
  - tkinter
  - tqdm

## Installation

1. Clone this repository or download the source code.
2. Install the required packages:

`pip install -r requirements.txt`

## Configuration

Before running the application, update the following constants in `config/settings.py`:

- `PDF_SOURCE`: Path to the source directory for scanned documents
- `PHOTO_SOURCE_BASE`: Path to the source directory for photos
- `DESTINATION_BASE`: Base path for the destination directories

## Usage

Run the main script to start the application:

`python src/main.py`

1. The application will first validate the directory structure.
2. If validation is successful, a GUI window will appear.
3. Choose either "Process Photos" or "Process Scans" to begin processing.
4. The application will move files to their appropriate destinations based on job numbers.
5. Progress will be displayed in the console, and a completion message will appear when finished.

## Logging

The application logs all operations to `file_processing.log` in the project root directory. Consult this log for detailed information about each run, including any errors or warnings.

## Project Structure

```text
file_processing_project/
│
├── src/
│ ├── init.py
│ ├── main.py
│ ├── gui.py
│ ├── file_operations.py
│ ├── logging_config.py
│ └── utils.py
│
├── config/
│ └── settings.py
│
├── logs/
│ └── file_processing.log
│
├── requirements.txt
└── README.md
```

## Troubleshooting

- If you encounter "File not found" errors, ensure all source and destination paths are correctly set in `config/settings.py`.
- For permission errors, check that the application has the necessary read/write permissions for all involved directories.

## Contributing

Contributions to improve the application are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

[MIT License]

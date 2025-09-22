
## File_Organizer.py

This script organizes files in a specified directory by their file extensions. It performs the following tasks:

- Scans the given directory for files.
- Creates folders named after each file extension.
- Moves files into their corresponding extension-named folders.
- Files without extensions are placed into a folder named "Other".


### Usage

Run the script with the path to the folder as a command-line argument or enter the path when prompted.

***

## File_Access_Tracker.py

This script gathers and stores metadata about files in a specified directory. It:

- Reads or creates a metadata JSON file listing file names, extensions, sizes, and timestamps for creation, modification, and access.
- Provides summary info such as total files, largest file, and counts of files by extension.
- Saves metadata to `metadata.json` and creates a ZIP archive of the folder contents.


### Usage

Run the script with the path to the folder as a command-line argument or enter the path when prompted.

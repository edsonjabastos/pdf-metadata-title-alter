# PDF Metadata Updater

This script scans a specified folder and its subfolders for PDF files and updates their metadata title to match their respective filenames.

## Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Setup Instructions

1. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   ```

2. **Activate the Virtual Environment**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Install Required Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Place the PDF files that need their title metadata updated into a folder named `pdfs` in the same directory as the script.
2. Run the script with:
   ```sh
   python main.py
   ```
3. Enter the path of the `pdfs` folder when prompted.

## Notes
- The script will recursively scan all subfolders within the specified folder.
- It updates the metadata title of each PDF to match its filename (without extension).

## Troubleshooting
- If you encounter errors, ensure that the `pdfs` folder exists and contains valid PDF files.
- Check that the required dependencies are installed correctly.

## License
This project is released under the MIT License.

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:edsonjabastos/pdf-metadata-title-alter.git
git push -u origin main
<<<<<<< HEAD
# table-viewer
Table Viewer with Filtering, Searching, and PDF Export
=======
# Table Viewer with Filtering, Searching, and PDF Export

## Overview

This is a Flask web application that allows you to browse tabular data files (CSV, Excel, SAS formats) with features such as:

- Display of first 50 rows preview, with option to show full table.
- Filtering by the second column using a dropdown list of unique values.
- Exporting the currently displayed table to a PDF file with pagination.
- Automatic hiding of the "Show All Rows" button when fewer than 50 rows are shown.
- Navigation back to the main file list page.

## Dependencies

This project uses the following Python packages:

- Python >= 3.10
- Flask >= 2.3.0 — web framework
- pandas >= 2.0.0 — data handling
- pyreadstat >= 1.2.0 — reading SAS files
- openpyxl >= 3.1.0 — Excel support for pandas
- Jinja2 >= 3.1.0 — templating 

These are listed in `requirements.txt`.

## Installation

1. Clone the repository:

git clone https://github.com/d-komissarchik/table-viewer

2. Create and activate a virtual environment (recommended):

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Put your data files (CSV, XLSX, SAS, etc.) into the `TabularViewer` folder (or the folder configured in your app).

## Running the Application

Start the Flask server:

python app.py

Open your browser and go to:

http://127.0.0.1:5000/

## Usage

- Select a file to view from the list.
- Use the filter dropdown to filter by the second column's values.
- Click "Show All Rows" to expand the table if it has more than 50 rows.
- Export the currently visible table to PDF with pagination using the "Export to PDF" button.
- Use "Back to file list" to return to the main page.

## Project Structure

.
├── app.py               # Main Flask application code
├── .gitignore           # Ignore Git files
├── requirements.txt     # Python dependencies
├── TabularViewer/       # Folder with data files
├── templates/
│   └── table.html       # Table view template with filtering, sorting, PDF export
│   └── index.html       # Main page listing available files
└── README.md            # This documentation file

## Notes

- Filtering works only on the second column.
- PDF export uses jsPDF library included via CDN.
- Make sure your data files have consistent formats for best results.
- Unable to read CPORT format.


>>>>>>> bc530b5 (first commit)

import os
from flask import Flask, render_template
import pandas as pd
import pyreadstat

app = Flask(__name__)

DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'TabularViewer')


@app.route('/')
def index():
    files = [
        file for file in os.listdir(DATA_FOLDER)
        if file.endswith(('sas7bdat', 'xpt', 'xlsx', 'csv'))
    ]
    return render_template(
        'index.html',
        files=files
    )


@app.route('/view_table/<filename>')
def view_table(filename):
    filepath = os.path.join(DATA_FOLDER, filename)

    try:
        with open(filepath, 'rb') as f:
            header = f.read(256).decode(errors='ignore')
            if 'COMPRESSED' in header.upper():
                return f'File {filename} is in CPORT format and cannot be read.', 400
    except Exception as e:
        return f'Error while checking file: {filename}: {e}'

    try:
        if filename.endswith('.sas7bdat'):
            df, meta = pyreadstat.read_sas7bdat(filepath)
        elif filename.endswith('.xpt'):
            df, meta = pyreadstat.read_xport(filepath)
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(filepath)
        elif filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        else:
            return f'Unsupported file format: {filename}', 400
    except Exception as e:
        return f'Failed to read file {filename}: {e}'

    return render_template(
        'table.html',
        filename=filename,
        short_table=df.head(51).to_html(classes='data'),
        full_table=df.to_html(classes='data'),
        show_button=len(df) > 50
    )


if __name__ == '__main__':
    app.run()

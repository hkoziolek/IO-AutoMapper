import os
import csv
import pandas as pd
from src.config.constants import IO_LIST_COLUMNS

def write_csv(filename, rows):
    """
    Write the generated list of I/O items to a CSV file.
    """
    # Create directory if it doesn't exist
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        
    # Use column headers from constants
    fieldnames = IO_LIST_COLUMNS
    
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def write_excel(filename, rows):
    """
    Write the generated list of I/O items to an Excel file.
    Requires pandas library to be installed.
    """
    # Create directory if it doesn't exist
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(rows)
    
    # Create Excel writer object
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    
    # Write DataFrame to Excel
    df.to_excel(writer, sheet_name='IO List', index=False)
    
    # Get the xlsxwriter workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['IO List']
    
    # Add some formatting
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#D3D3D3',  # Light gray background
        'border': 1
    })
    
    # Apply the header format to the header row
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
    # Auto-fit columns
    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        worksheet.set_column(col_idx, col_idx, column_width + 2)
    
    # Close the Excel writer
    writer.close()

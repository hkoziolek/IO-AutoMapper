import os
from src.generators.io_generator import generate_io_list
from src.utils.file_writers import write_csv, write_excel
from src.config.constants import NUMBER_OF_ROWS

def main():
    """Main entry point for the IO List Generator application."""
    io_list = generate_io_list(num_entries=NUMBER_OF_ROWS)
    
    # Define output paths
    output_dir = os.path.join("io_list_generation", "output")
    csv_file = os.path.join(output_dir, "io_list.csv")
    excel_file = os.path.join(output_dir, "io_list.xlsx")
    
    # Write CSV file
    write_csv(csv_file, io_list)
    print(f"I/O list written to {csv_file}.")

    # Try to write Excel file
    try:
        write_excel(excel_file, io_list)
        print(f"I/O list written {excel_file}.")
    except Exception as e:
        print(f"Error writing Excel file: {str(e)}")

if __name__ == "__main__":
    main()

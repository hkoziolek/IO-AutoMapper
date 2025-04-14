import os
import unittest
import tempfile
from src.generators.io_generator import generate_io_list
from src.utils.file_writers import write_csv, write_excel

class TestFileWriters(unittest.TestCase):
    
    def setUp(self):
        """Create temporary data for tests."""
        self.test_data = generate_io_list(num_entries=10)
        # Create a temporary directory for test files
        self.temp_dir = tempfile.mkdtemp()
        
    def test_csv_writer(self):
        """Test that the CSV writer creates a valid file."""
        csv_file = os.path.join(self.temp_dir, "test_io_list.csv")
        write_csv(csv_file, self.test_data)
        
        # Verify file was created and has content
        self.assertTrue(os.path.exists(csv_file))
        self.assertTrue(os.path.getsize(csv_file) > 0)
        
    def test_excel_writer(self):
        """Test that the Excel writer creates a valid file."""
        try:
            # Skip test if pandas/xlsxwriter not available
            import pandas
            import xlsxwriter
            
            excel_file = os.path.join(self.temp_dir, "test_io_list.xlsx")
            write_excel(excel_file, self.test_data)
            
            # Verify file was created and has content
            self.assertTrue(os.path.exists(excel_file))
            self.assertTrue(os.path.getsize(excel_file) > 0)
            
        except ImportError:
            print("Skipping Excel writer test - required libraries not available")

if __name__ == '__main__':
    unittest.main()

import unittest
from src.generators.io_generator import generate_io_list
from src.generators.signal_types import generate_data_signal_type, generate_engineering_unit

class TestGenerators(unittest.TestCase):
    
    def test_io_list_generation(self):
        """Test that the IO list generator creates the correct number of entries."""
        num_entries = 50
        io_list = generate_io_list(num_entries=num_entries)
        self.assertEqual(len(io_list), num_entries)
        
    def test_data_signal_types(self):
        """Test that signal type generator returns expected types for different IO types."""
        ai_type = generate_data_signal_type("AI")
        di_type = generate_data_signal_type("DI")
        do_type = generate_data_signal_type("DO")
        
        # Check that we get expected signal type categories
        self.assertIn(ai_type, ["4-20 mA", "0-10 V", "RTD", "Thermocouple"])
        self.assertIn(di_type, ["24 VDC", "Dry Contact", "Pulse"])
        self.assertIn(do_type, ["24 VDC", "Relay", "Solid State"])
        
    def test_engineering_units(self):
        """Test that engineering units are appropriate for signal types."""
        # Digital signals should return N/A
        di_unit = generate_engineering_unit("DI", "24 VDC", "High level alarm")
        self.assertEqual(di_unit, "N/A")
        
        # Check temperature signals
        temp_unit = generate_engineering_unit("AI", "RTD", "Temperature reading")
        self.assertEqual(temp_unit, "Celcius")

if __name__ == '__main__':
    unittest.main()

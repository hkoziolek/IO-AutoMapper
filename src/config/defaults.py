import re

# Configuration constants
PROMPT_TEMPLATES_DIR = "prompt_templates_LIB1"
ENABLE_GROUND_TRUTH_CHECK = True

# Alternative configurations (commented out but available)
ALTERNATIVE_CONFIGS = {
    "DEVLIST1": {
        "file": "test-data/generated_io_list_1.xlsx",
        "columns": [
            "Tagname", 
            "I/O Type", 
            "Unit Description", 
            "Field Device Description", 
            "Signal Description"
        ],
        "signal_tag_column": 0,
        "device_description_column": 3,
        "tagname_pattern": re.compile(
            # Assumed tagname pattern: 100-XY100-UA1 (with 100-XY100 referring to device)
            r'^(?P<prefix>\d{3}-[A-Za-z0-9]+)-(?P<suffix>[A-Za-z0-9]{2,5})$'
        ),
        "start_line": 1,
        "end_line": 300
    },
    "DEVLIST2": {
        "file": "test-data/generated_io_list_2.xlsx",
        "columns": [
            "Tag", 
            "Type of Signal", 
            "Area", 
            "DESC", 
            "SERVICE"
        ],
        "signal_tag_column": 0,
        "device_description_column": 3,
        "tagname_pattern": re.compile(
            r'^(?P<prefix>[A-Za-z0-9]+).(?P<suffix>[A-Za-z0-9]{2,5})$'
        ),
        "start_line": 1,
        "end_line": 300
    },
    "DEVLIST3": {
        "file": "test-data/generated_io_list_3.xlsx",
        "columns": [
            "Reference", 
            "Analog/Digital", 
            "Module", 
            "Device", 
            "I/O Function",
        ],
        "signal_tag_column": 0,
        "device_description_column": 3,
        "tagname_pattern": re.compile(
            r'^(?P<prefix>[A-Za-z0-9]+-[A-Za-z0-9]+)_(?P<suffix>[A-Za-z0-9]{2,5})$'
        ),
        "start_line": 1,
        "end_line": 300
    }
}

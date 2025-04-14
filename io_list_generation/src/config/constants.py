# Example list of plant areas in ascending order; expand/adjust as needed
AREAS_1 = ["101", "102", "202", "203", "301", "302", "401", "501", "601", "602"]
AREAS_2 = ["040", "070", "090", "375", "379", "382", "440", "630", "920", "921"]
AREAS_3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
AREAS = AREAS_3

# Ensure the AREAS list is sorted in ascending order
AREAS.sort()

# Number of I/O points to generate
NUMBER_OF_ROWS = 300

# Column headers for output files
IO_LIST_COLUMNS_1 = [
    "Tagname",
    "I/O Type",
    "Data/Signal Type",
    "Engineering Unit",
    "Unit Description",
    "Field Device Description",
    "Signal Description",
    "Module Channel",
    "P&ID Reference",
    "Process Unit",
    "Min Range",
    "Max Range"
]

IO_LIST_COLUMNS_2 = [
    "Tag",
    "Type of Signal",
    "Data/Signal Type",
    "Physical",
    "Area",
    "DESC",
    "SERVICE",
    "Channel",
    "DIAG",
    "AREA ID",
    "L",
    "H"
]

IO_LIST_COLUMNS_3 = [
    "Reference",
    "Analog/Digital",
    "Connection",
    "Eng. Unit",
    "Module",
    "Device",
    "I/O Function",
    "Cabinet Mapping",
    "P&ID",
    "Module Reference",
    "Low Range",
    "High Range"
]

IO_LIST_COLUMNS = IO_LIST_COLUMNS_3

# Tagname templates
# Available placeholders:
# {area} - Area code
# {dev_type} - Device type code
# {dev_num} - Device number (will be formatted as specified, e.g., {dev_num:03d})
# {suffix} - Signal suffix
# {unit_num} - Unit number

TAGNAME_TEMPLATES = {
    "STANDARD": "{area}-{dev_type}{dev_num:03d}-{suffix}",     # Example: A1-FIT001-PV
    "EXTENDED": "{area}{unit_num}-{dev_type}{dev_num:03d}-{suffix}",  # Example: A1100-FIT001-PV
    "SIMPLE": "{dev_type}{dev_num:03d}_{suffix}",               # Example: FIT001_PV
    "DEVLIST2": "{area}{unit_num}{dev_type}{dev_num:03d}.{suffix}",  # Example: A1100FIT001.PV
    "DEVLIST3": "1290-{dev_type}{dev_num:04d}_{suffix}"  # Example: 1290FIT0001_PV
}
ACTIVE_TAGNAME_TEMPLATE = "DEVLIST3"  # Active tagname template

DEVICE_DEFINITIONS_1 = "device_definitions_1"
DEVICE_DEFINITIONS_2 = "device_definitions_2"
DEVICE_DEFINITIONS_3 = "device_definitions_3"
ACTIVE_DEVICE_DEFINITIONS = DEVICE_DEFINITIONS_3

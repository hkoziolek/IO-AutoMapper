from src.generators.process_units import generate_process_units
from src.generators.signal_types import (
    generate_data_signal_type, 
    generate_engineering_unit, 
    generate_module_channel, 
    generate_p_and_id_reference,
    generate_range_values
)
from src.config.constants import IO_LIST_COLUMNS, TAGNAME_TEMPLATES, ACTIVE_TAGNAME_TEMPLATE

def generate_tagname(template_name, **kwargs):
    """
    Generate a tagname based on the specified template.
    
    Args:
        template_name: The name of the template to use from TAGNAME_TEMPLATES
        **kwargs: The values to substitute into the template
    
    Returns:
        A formatted tagname string
    """
    template = TAGNAME_TEMPLATES.get(template_name, TAGNAME_TEMPLATES[ACTIVE_TAGNAME_TEMPLATE])
    return template.format(**kwargs)

def generate_io_list(num_entries=20, tagname_template=ACTIVE_TAGNAME_TEMPLATE):
    """
    Generate a list of I/O items with plausible content.
    Returns a list of dictionaries, each dictionary representing one row.
    
    Args:
        num_entries: Number of I/O entries to generate
        tagname_template: The template to use for tagname generation
    """
    rows = []
    index = 1  # used for module channel numbering
    used_tagnames = set()  # Track used tagnames to prevent duplicates
    
    # Track device counts by area and type for tagname numbering
    device_counters = {}  # Format: {area: {dev_type: count}}
    
    # Generate process units that will contain related devices
    device_queue = generate_process_units(num_entries)
    
    # Process each device in our queue
    for device in device_queue:
        area = device["area"]
        dev_type = device["device_type"]
        dev_def = device["device_def"]
        unit_number = device["unit_number"]
        unit_description = device["unit_description"]
        
        # Initialize area counter if needed
        if area not in device_counters:
            device_counters[area] = {}
            
        # Initialize device type counter if needed
        if dev_type not in device_counters[area]:
            device_counters[area][dev_type] = 1
        else:
            device_counters[area][dev_type] += 1
            
        # Get the device number for this area/device type combination
        device_number = device_counters[area][dev_type]
        
        # For each suffix in that device's definition, generate a row
        for suffix, io_type, signal_desc in dev_def["suffixes"]:
            # Generate tagname using the template system
            tagname = generate_tagname(
                tagname_template,
                area=area,
                dev_type=dev_type,
                dev_num=device_number,
                suffix=suffix,
                unit_num=unit_number
            )
            
            data_type = generate_data_signal_type(io_type)
            eng_unit = generate_engineering_unit(io_type, data_type, signal_desc)
            
            # Create a field device description without the unit description
            field_device_desc = f"{dev_def['description']}"

            # Generate range information for analog signals
            min_value, max_value = generate_range_values(io_type, signal_desc, eng_unit)

            # Create a unique device identifier for P&ID reference consistency
            device_id = f"{area}-{dev_type}-{device_number}"

            # Create a dictionary with keys matching IO_LIST_COLUMNS
            row = {
                IO_LIST_COLUMNS[0]: tagname,                    # Tagname
                IO_LIST_COLUMNS[1]: io_type,                    # I/O Type
                IO_LIST_COLUMNS[2]: data_type,                  # Data/Signal Type
                IO_LIST_COLUMNS[3]: eng_unit,                   # Engineering Unit
                IO_LIST_COLUMNS[4]: unit_description,           # Unit Description
                IO_LIST_COLUMNS[5]: field_device_desc,          # Field Device Description
                IO_LIST_COLUMNS[6]: signal_desc,                # Signal Description
                IO_LIST_COLUMNS[7]: generate_module_channel(io_type, index),  # Module Channel
                IO_LIST_COLUMNS[8]: generate_p_and_id_reference(device_id),  # P&ID Reference
                IO_LIST_COLUMNS[9]: f"{area}-{unit_number}",    # Process Unit
                IO_LIST_COLUMNS[10]: min_value,                 # Min Range
                IO_LIST_COLUMNS[11]: max_value                  # Max Range
            }

            rows.append(row)
            index += 1
            
            # If we've reached/exceeded the target, we can stop early
            if len(rows) >= num_entries:
                return rows[:num_entries]  # Truncate to exact number requested

    return rows

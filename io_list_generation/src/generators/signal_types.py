import random

def generate_data_signal_type(iotype):
    """
    Return a plausible data/signal type based on the I/O type.
    For instance, AI might typically have 4-20 mA, RTD, etc.
    DO/DI might have 24 VDC, etc.
    """
    if iotype == "AI":
        return random.choice(["4-20 mA", "0-10 V", "RTD", "Thermocouple"])
    elif iotype == "DI":
        return random.choice(["24 VDC", "Dry Contact", "Pulse"])
    else:  # DO
        return random.choice(["24 VDC", "Relay", "Solid State"])

def generate_engineering_unit(io_type: str, data_type: str, signal_description: str) -> str:
    """
    Return a plausible engineering unit depending on the I/O type and signal.
    """
    if io_type in ["DI", "DO"]:
        return "N/A"
    # If AI, check if it's temperature
    if "Temp" in signal_description or "Temperature" in signal_description:
        return "Celcius"
    if "Thermocouple" in data_type or "RTD" in data_type:
        return "Celcius"
    
    # Use a single unit per metric for consistency
    if "Level" in signal_description:
        return "m"
    elif "Flow" in signal_description:
        return "m3/h"
    elif "Pressure" in signal_description:
        return "bar"
    elif "Temperature" in signal_description:
        return "Celsius"
    else:
        return "N/A"

def generate_module_channel(iotype, index):
    """
    Return a plausible module channel name, e.g. AI-01, DI-05, DO-02, based on I/O type.
    The 'index' parameter is used to generate a unique channel number.
    """
    channel_num = f"{index % 16 + 1:02d}"  # More realistic: channels typically 1-16 per card
    card_num = f"{(index // 16) + 1:02d}"
    return f"{iotype}{card_num}-{channel_num}"

def generate_p_and_id_reference(device_id=None):
    """
    Return a P&ID reference, e.g. P&ID-001 up to P&ID-050.
    If device_id is provided, ensures all signals from the same device
    get the same P&ID reference.
    """
    # Dictionary to store device_id to P&ID mappings
    if not hasattr(generate_p_and_id_reference, "device_mappings"):
        generate_p_and_id_reference.device_mappings = {}
    
    # If no device_id is provided or it's a new device, generate a new reference
    if device_id is None or device_id not in generate_p_and_id_reference.device_mappings:
        ref_num = random.randint(1, 50)
        pid_ref = f"P&ID-{ref_num:03d}"
        
        # Store the mapping if we have a device_id
        if device_id is not None:
            generate_p_and_id_reference.device_mappings[device_id] = pid_ref
        return pid_ref
    
    # Return existing P&ID reference for known devices
    return generate_p_and_id_reference.device_mappings[device_id]

def generate_range_values(io_type, signal_description, eng_unit):
    """
    Generate plausible min/max range values based on the I/O type, signal description, and engineering unit.
    Returns a tuple of (min_value, max_value)
    """
    # For digital signals, return N/A
    if io_type in ["DI", "DO"]:
        return "N/A", "N/A"
    
    # For analog signals, generate appropriate ranges
    if "Temperature" in signal_description or eng_unit == "Celsius":
        return str(random.randint(-20, 30)), str(random.randint(80, 150))
    elif "Level" in signal_description:
        return "0", str(random.randint(5, 30))
    elif "Flow" in signal_description:
        return "0", str(random.randint(100, 500))
    elif "Pressure" in signal_description:
        return "0", str(random.randint(6, 25))
    else:
        return "0", "100"  # Default range

import random
from src.config.constants import AREAS
#from io_list_generation.src.config.device_definitions_1 import DEVICE_DEFINITIONS, PROCESS_UNITS
from src.config.config_loader import load_device_definitions, load_process_units


def generate_process_units(num_entries):
    """
    Generate process units distributed across plant areas.
    Returns a list of devices that should be created.
    """
    device_queue = []
    entries_remaining = num_entries
    
    device_definitions = load_device_definitions()
    process_units = load_process_units()

    # Keep track of unit numbers per area
    area_unit_counters = {area: 1 for area in AREAS}
    
    # Track current area index to ensure we process areas in ascending order
    current_area_index = 0
    
    while entries_remaining > 0:
        # Add a failsafe to prevent infinite loops when remaining entries are very small
        if entries_remaining < 3:
            # For the last few entries, create simple standalone devices
            # Use the current area instead of a random one
            current_area = AREAS[current_area_index]
            
            # Pick a device type with minimal signals
            simple_device_types = ["VC", "FN"]  # These typically have few signals
            dev_type = random.choice(simple_device_types)
            dev_def = device_definitions[dev_type]
            if isinstance(dev_def, list):
                dev_def = dev_def[0]
            
            unit_number = f"{area_unit_counters[current_area]:03d}"
            area_unit_counters[current_area] += 1
            
            # Take just enough signals to fill our quota
            for suffix, io_type, signal_desc in dev_def["suffixes"]:
                if entries_remaining <= 0:
                    break
                    
                single_device = {
                    "area": current_area,
                    "unit_number": unit_number,
                    "device_type": dev_type,
                    "device_def": dev_def,
                    "unit_type": "STANDALONE",
                    "unit_description": "Standalone device"
                }
                device_queue.append(single_device)
                entries_remaining -= 1
                
            # If we've processed all remaining entries, exit the loop
            if entries_remaining <= 0:
                break
            continue
            
        # Select an area - in sequential order with occasional repeat
        if not device_queue or random.random() < 0.3:  # 30% chance to move to next area
            current_area_index = (current_area_index + 1) % len(AREAS)
        
        current_area = AREAS[current_area_index]
        
        # Select a process unit type
        unit_type = random.choice(list(process_units.keys()))
        unit = process_units[unit_type]
        
        # Generate a unit number for this process unit
        unit_number = f"{area_unit_counters[current_area]:03d}"
        area_unit_counters[current_area] += 1
        
        # Track how many signals this unit will generate
        unit_signal_count = 0
        unit_devices = []
        
        # For each device type in this unit
        for device_spec in unit.get("devices", []):
            # Skip if not required and we randomly decide not to include it
            if not device_spec["required"] and random.random() < 0.4:
                continue
                
            # How many of this device type to include
            count = device_spec["count"]
            
            # For each device of this type
            for _ in range(count):
                device_type = device_spec["type"]
                dev_def = device_definitions[device_type]
                
                # Handle device variants
                if isinstance(dev_def, list):
                    dev_def = random.choice(dev_def)
                
                # Count how many signals this device will generate
                signal_count = len(dev_def["suffixes"])
                unit_signal_count += signal_count
                
                # Add to our list of devices to create
                unit_devices.append({
                    "area": current_area,
                    "unit_number": unit_number,
                    "device_type": device_type,
                    "device_def": dev_def,
                    "unit_type": unit_type,
                    "unit_description": unit["description"]
                })
        
        # If this unit would take us over our limit, try a different unit
        if unit_signal_count > entries_remaining:
            # Track failed attempts to prevent infinite loops
            failed_attempts = 0
            found_small_device = False
            
            if entries_remaining < 5:  # If we need just a few more signals
                # Find a small device with few signals
                for dev_type, def_data in device_definitions.items():
                    if isinstance(def_data, list):
                        for variant in def_data:
                            if len(variant["suffixes"]) <= entries_remaining:
                                single_device = {
                                    "area": current_area,
                                    "unit_number": unit_number,
                                    "device_type": dev_type,
                                    "device_def": variant,
                                    "unit_type": "STANDALONE",
                                    "unit_description": "Standalone device"
                                }
                                device_queue.append(single_device)
                                entries_remaining -= len(variant["suffixes"])
                                found_small_device = True
                                break
                        if found_small_device:
                            break
                    else:
                        if len(def_data["suffixes"]) <= entries_remaining:
                            single_device = {
                                "area": current_area,
                                "unit_number": unit_number,
                                "device_type": dev_type,
                                "device_def": def_data,
                                "unit_type": "STANDALONE",
                                "unit_description": "Standalone device"
                            }
                            device_queue.append(single_device)
                            entries_remaining -= len(def_data["suffixes"])
                            found_small_device = True
                            break
                
                # If we couldn't find any suitable device, break out to avoid infinite loop
                if not found_small_device:
                    failed_attempts += 1
                    
                    # After multiple failed attempts, just exit the loop
                    if failed_attempts >= 10:
                        print(f"Warning: Could not find suitable devices to reach exactly {num_entries} signals. " +
                              f"Generated {num_entries - entries_remaining} signals instead.")
                        break
            continue
            
        # Add all devices from this unit to our queue
        device_queue.extend(unit_devices)
        entries_remaining -= unit_signal_count
    
    return device_queue

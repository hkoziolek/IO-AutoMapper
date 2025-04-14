import importlib
from src.config.constants import ACTIVE_DEVICE_DEFINITIONS

def load_device_definitions():
    module_path = f"src.config.{ACTIVE_DEVICE_DEFINITIONS}"
    device_definitions_module = importlib.import_module(module_path)
    return device_definitions_module.DEVICE_DEFINITIONS

def load_process_units():
    module_path = f"src.config.{ACTIVE_DEVICE_DEFINITIONS}"
    process_units_module = importlib.import_module(module_path)
    return process_units_module.PROCESS_UNITS


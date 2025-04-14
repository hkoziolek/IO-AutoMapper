DEVICE_DEFINITIONS = {
    "LT": {
        "description": "Level Device",
        "suffixes": [
            ("LI", "AI", "Tank level")
        ]
    },
    "FT": {
        "description": "Flow Device",
        "suffixes": [
            ("FI", "AI", "Flow reading")
        ]
    },
    "TT": {
        "description": "Temperature Device",
        "suffixes": [
            ("TI", "AI", "Temperature reading")
        ]
    },
    "PT": {
        "description": "Pressure Device",
        "suffixes": [
            ("PI", "AI", "Pressure reading")
        ]
    },
    "PM": [
        {
            "description": "Pump Motor Basic",
            "suffixes": [
                ("XST", "DO", "Start pump"),
                ("XSP", "DO", "Stop pump"),
                ("XRC", "DO", "Remote control"),
                ("XRN", "DI", "Running status"),
                ("XPFA", "DI", "Power fault"),
                ("XOLA", "DI", "Overload alarm")
            ]
        },
        {
            "description": "Pump Motor Standard",
            "suffixes": [
                ("XST", "DO", "Start command"),
                ("XSP", "DO", "Stop command"),
                ("XRS", "DO", "Reset fault"),
                ("XRN", "DI", "Running status"),
                ("XHFA", "DI", "High flow alarm"),
                ("XOLA", "DI", "Overload alarm")
            ]
        },
        {
            "description": "Pump Motor Advanced",
            "suffixes": [
                ("XST", "DO", "Start motor"),
                ("XSP", "DO", "Stop motor"),
                ("XRC", "DO", "Remote mode"),
                ("XRN", "DI", "Running status"),
                ("XHTA", "DI", "High temp alarm"),
                ("XOLA", "DI", "Overload alarm")
            ]
        }
    ],
    "VC": {
        "description": "Valve Basic",
        "suffixes": [
            ("XOC", "DO", "Open valve"),
            ("XCC", "DO", "Close valve"),
            ("XOF", "DI", "Open status"),
            ("XCF", "DI", "Closed status")
        ]
    },
    "VC3": {
        "description": "Three-Way Valve",
        "suffixes": [
            ("XOC", "DO", "Open command"),
            ("XCC", "DO", "Close command"),
            ("XIC", "DO", "Mid position"),
            ("XOF", "DI", "Open status"),
            ("XCF", "DI", "Closed status"),
            ("XIF", "DI", "Mid status"),
            ("XMV", "DI", "Moving status"),
            ("XFT", "DI", "Fault status"),
            ("POS", "AI", "Position value"),
            ("XRS", "DO", "Reset fault")
        ]
    },
    "FN": {
        "description": "Fan Unit",
        "suffixes": [
            ("XST", "DO", "Start fan"),
            ("XSP", "DO", "Stop fan"),
            ("XRN", "DI", "Running status")
        ]
    },
    "CA": {
        "description": "Compressor Unit",
        "suffixes": [
            ("XST", "DO", "Start compressor"),
            ("XSP", "DO", "Stop compressor"),
            ("XRN", "DI", "Running status"),
            ("XPFA", "DI", "Power fault")
        ]
    },
    "VFD": [
        {
            "description": "Variable Drive Basic",
            "suffixes": [
                ("XST", "DO", "Start drive"),
                ("XSP", "DO", "Stop drive"),
                ("XRS", "DO", "Reset drive"),
                ("XRN", "DI", "Running status"),
                ("XFT", "DI", "Fault status"),
                ("SC", "AO", "Speed control"),
                ("SI", "AI", "Speed feedback")
            ]
        },
        {
            "description": "Variable Drive Full",
            "suffixes": [
                ("XST", "DO", "Start drive"),
                ("XSP", "DO", "Stop drive"),
                ("XRS", "DO", "Reset drive"),
                ("XRC", "DO", "Remote mode"),
                ("XRN", "DI", "Running status"),
                ("XFT", "DI", "Fault status"),
                ("SC", "AO", "Speed control"),
                ("SI", "AI", "Speed feedback"),
                ("CI", "AI", "Current feedback"),
                ("XMA", "DI", "Manual mode")
            ]
        }
    ],
    "HTR": [
        {
            "description": "Heater Simple",
            "suffixes": [
                ("XST", "DO", "Start heater"),
                ("XRN", "DI", "Running status")
            ]
        },
        {
            "description": "Heater Full",
            "suffixes": [
                ("XST", "DO", "Start heater"),
                ("XSP", "DO", "Stop heater"),
                ("XRN", "DI", "Running status"),
                ("TC", "AO", "Temp setpoint"),
                ("TI", "AI", "Temp feedback")
            ]
        }
    ],
    "MX": [
        {
            "description": "Mixer Simple",
            "suffixes": [
                ("XST", "DO", "Start mixer"),
                ("XRN", "DI", "Running status"),
                ("XOLA", "DI", "Overload alarm")
            ]
        },
        {
            "description": "Mixer Full",
            "suffixes": [
                ("XST", "DO", "Start mixer"),
                ("XSP", "DO", "Stop mixer"),
                ("XRN", "DI", "Running status"),
                ("XOLA", "DI", "Overload alarm"),
                ("SC", "AO", "Speed control"),
                ("TI", "AI", "Temp feedback")
            ]
        }
    ],
    "CB": [
        {
            "description": "Conveyor Full",
            "suffixes": [
                ("XFWD", "DO", "Forward command"),
                ("XREV", "DO", "Reverse command"),
                ("XSTP", "DO", "Stop command"),
                ("XFWF", "DI", "Forward status"),
                ("XRVF", "DI", "Reverse status"),
                ("XRDY", "DI", "Ready status"),
                ("XFTA", "DI", "Fault status"),
                ("SC", "AO", "Speed control"),
                ("SI", "AI", "Speed feedback"),
                ("XOLA", "DI", "Overload alarm")
            ]
        },
        {
            "description": "Conveyor Basic",
            "suffixes": [
                ("XFWD", "DO", "Forward command"),
                ("XREV", "DO", "Reverse command"),
                ("XSTP", "DO", "Stop command"),
                ("XFWF", "DI", "Forward status"),
                ("XRVF", "DI", "Reverse status"),
                ("XFTA", "DI", "Fault status")
            ]
        }
    ]
}

# Process units define logical groupings of devices that interact with each other
PROCESS_UNITS = {
    "PUMP_STATION": {
        "description": "Pumping system",
        "devices": [
            {"type": "PM", "count": 1, "required": True},   # Pump
            {"type": "FT", "count": 1, "required": True},   # Flow sensor
            {"type": "PT", "count": 1, "required": True},   # Pressure sensor
            {"type": "VC", "count": 1, "required": False},  # Optional valve
        ]
    },
    "TANK_SYSTEM": {
        "description": "Storage tank",
        "devices": [
            {"type": "LT", "count": 1, "required": True},   # Level sensor
            {"type": "TT", "count": 1, "required": False},  # Optional temp sensor
            {"type": "VC", "count": 2, "required": False},  # Optional valves
        ]
    },
    "TRANSFER_SYSTEM": {
        "description": "Material transfer",
        "devices": [
            {"type": "PM", "count": 1, "required": True},   # Pump
            {"type": "FT", "count": 1, "required": True},   # Flow sensor
            {"type": "VC", "count": 2, "required": True},   # Valves
        ]
    },
    "COMPRESSOR_UNIT": {
        "description": "Air compression",
        "devices": [
            {"type": "CA", "count": 1, "required": True},   # Compressor
            {"type": "PT", "count": 2, "required": True},   # Pressure sensors
            {"type": "TT", "count": 1, "required": True},   # Temp sensor
        ]
    },
    "VENTILATION_SYSTEM": {
        "description": "Air handling",
        "devices": [
            {"type": "FN", "count": 1, "required": True},   # Fan
            {"type": "TT", "count": 1, "required": True},   # Temp sensor
        ]
    },
    "MIXING_SYSTEM": {
        "description": "Material mixing",
        "devices": [
            {"type": "MX", "count": 1, "required": True},   # Mixer
            {"type": "TT", "count": 1, "required": True},   # Temp sensor
            {"type": "LT", "count": 1, "required": True},   # Level sensor
            {"type": "VC", "count": 2, "required": False},  # Optional valves
        ]
    },
    "HEATING_SYSTEM": {
        "description": "Process heating",
        "devices": [
            {"type": "HTR", "count": 1, "required": True},  # Heater
            {"type": "TT", "count": 2, "required": True},   # Temp sensors
            {"type": "FT", "count": 1, "required": False},  # Optional flow sensor
        ]
    },
    "VFD_PUMP_SYSTEM": {
        "description": "Variable speed pump",
        "devices": [
            {"type": "VFD", "count": 1, "required": True},  # Variable drive
            {"type": "FT", "count": 1, "required": True},   # Flow sensor
            {"type": "PT", "count": 1, "required": True},   # Pressure sensor
        ]
    },
    "BATCHING_SYSTEM": {
        "description": "Material batching",
        "devices": [
            {"type": "VC3", "count": 2, "required": True},  # Three-way valves
            {"type": "MX", "count": 1, "required": False},  # Optional mixer
        ]
    },
    "MATERIAL_HANDLING": {
        "description": "Material transport",
        "devices": [
            {"type": "CB", "count": 1, "required": True},   # Conveyor
            {"type": "VC", "count": 1, "required": False},  # Optional valve
            {"type": "FT", "count": 1, "required": False},  # Optional flow sensor
            {"type": "LT", "count": 2, "required": False},  # Optional level sensors
        ]
    },
    "PACKAGING_LINE": {
        "description": "Product packaging",
        "devices": [
            {"type": "CB", "count": 2, "required": True},   # Conveyors
            {"type": "PT", "count": 1, "required": False},  # Optional pressure sensor
            {"type": "FT", "count": 1, "required": False},  # Optional flow sensor
        ]
    }
}

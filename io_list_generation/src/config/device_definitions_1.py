DEVICE_DEFINITIONS = {
    "LT": {
        "description": "Level Transmitter",
        "suffixes": [
            ("LI", "AI", "Tank level measurement")
        ]
    },
    "FT": {
        "description": "Flow Transmitter",
        "suffixes": [
            ("FI", "AI", "Flow rate measurement")
        ]
    },
    "TT": {
        "description": "Temperature Transmitter",
        "suffixes": [
            ("TI", "AI", "Temperature reading")
        ]
    },
    "PT": {
        "description": "Pressure Transmitter",
        "suffixes": [
            ("PI", "AI", "Pressure reading")
        ]
    },
    "PM": [
        {
            "description": "Pump Motor Starter Variant 1",
            "suffixes": [
                ("XST", "DO", "Pump start command"),
                ("XSP", "DO", "Pump stop command"),
                ("XRC", "DO", "Remote control enable signal"),
                ("XRN", "DI", "Pump running feedback"),
                ("XPFA", "DI", "Power failure detected"),
                ("XOLA", "DI", "Motor overload alarm")
            ]
        },
        {
            "description": "Pump Motor Starter Variant 2",
            "suffixes": [
                ("XST", "DO", "Start pump command"),
                ("XSP", "DO", "Stop pump command"),
                ("XRS", "DO", "Reset fault command"),
                ("XRN", "DI", "Running status feedback"),
                ("XHFA", "DI", "High flow detected"),
                ("XOLA", "DI", "Overload condition alarm")
            ]
        },
        {
            "description": "Pump Motor Starter Variant 3",
            "suffixes": [
                ("XST", "DO", "Start motor command"),
                ("XSP", "DO", "Stop motor command"),
                ("XRC", "DO", "Enable remote control"),
                ("XRN", "DI", "Motor running feedback"),
                ("XHTA", "DI", "High temperature detected"),
                ("XOLA", "DI", "Overload protection triggered")
            ]
        }
    ],
    "VC": {
        "description": "Valve Actuator",
        "suffixes": [
            ("XOC", "DO", "Open valve command"),
            ("XCC", "DO", "Close valve command"),
            ("XOF", "DI", "Valve open status feedback"),
            ("XCF", "DI", "Valve closed status feedback")
        ]
    },
    "VC3": {
        "description": "Three-Position Valve Actuator",
        "suffixes": [
            ("XOC", "DO", "Command to open valve"),
            ("XCC", "DO", "Command to close valve"),
            ("XIC", "DO", "Command to move to intermediate position"),
            ("XOF", "DI", "Feedback: valve is fully opened"),
            ("XCF", "DI", "Feedback: valve is fully closed"),
            ("XIF", "DI", "Feedback: valve is in intermediate position"),
            ("XMV", "DI", "Feedback: valve is moving"),
            ("XFT", "DI", "Valve actuator fault"),
            ("POS", "AI", "Valve position feedback (0-100%)"),
            ("XRS", "DO", "Reset valve fault")
        ]
    },
    "FN": {
        "description": "Fan Starter",
        "suffixes": [
            ("XST", "DO", "Fan start command"),
            ("XSP", "DO", "Fan stop command"),
            ("XRN", "DI", "Fan running feedback")
        ]
    },
    "CA": {
        "description": "Compressor Actuator",
        "suffixes": [
            ("XST", "DO", "Compressor start command"),
            ("XSP", "DO", "Compressor stop command"),
            ("XRN", "DI", "Compressor running feedback"),
            ("XPFA", "DI", "Power failure detected")
        ]
    },
    "VFD": [
        {
            "description": "Variable Frequency Drive Basic",
            "suffixes": [
                ("XST", "DO", "Start VFD command"),
                ("XSP", "DO", "Stop VFD command"),
                ("XRS", "DO", "Reset VFD fault"),
                ("XRN", "DI", "VFD running feedback"),
                ("XFT", "DI", "Fault status signal"),
                ("SC", "AO", "Speed control signal"),
                ("SI", "AI", "Speed feedback signal")
            ]
        },
        {
            "description": "Variable Frequency Drive Extended",
            "suffixes": [
                ("XST", "DO", "Command to start VFD"),
                ("XSP", "DO", "Command to stop VFD"),
                ("XRS", "DO", "Command to reset fault"),
                ("XRC", "DO", "Enable remote control"),
                ("XRN", "DI", "Feedback: VFD is running"),
                ("XFT", "DI", "Feedback: fault detected"),
                ("SC", "AO", "Speed control output"),
                ("SI", "AI", "Speed indication signal"),
                ("CI", "AI", "Current feedback signal"),
                ("XMA", "DI", "Manual mode active")
            ]
        }
    ],
    "HTR": [
        {
            "description": "Heater Element Basic",
            "suffixes": [
                ("XST", "DO", "Heater start command"),
                ("XRN", "DI", "Heater running feedback")
            ]
        },
        {
            "description": "Heater Element Advanced",
            "suffixes": [
                ("XST", "DO", "Start heater command"),
                ("XSP", "DO", "Stop heater command"),
                ("XRN", "DI", "Running status feedback"),
                ("TC", "AO", "Temperature control signal"),
                ("TI", "AI", "Temperature feedback signal")
            ]
        }
    ],
    "MX": [
        {
            "description": "Mixer Simple",
            "suffixes": [
                ("XST", "DO", "Mixer start command"),
                ("XRN", "DI", "Mixer running feedback"),
                ("XOLA", "DI", "Overload alarm triggered")
            ]
        },
        {
            "description": "Mixer Advanced",
            "suffixes": [
                ("XST", "DO", "Start mixer command"),
                ("XSP", "DO", "Stop mixer command"),
                ("XRN", "DI", "Feedback: mixer is running"),
                ("XOLA", "DI", "Alarm: overload condition"),
                ("SC", "AO", "Speed control signal"),
                ("TI", "AI", "Temperature feedback")
            ]
        }
    ],
    "CB": [
        {
            "description": "Conveyor Belt",
            "suffixes": [
                ("XFWD", "DO", "Forward start command"),
                ("XREV", "DO", "Reverse start command"),
                ("XSTP", "DO", "Stop command"),
                ("XFWF", "DI", "Forward running feedback"),
                ("XRVF", "DI", "Reverse running feedback"),
                ("XRDY", "DI", "Ready status"),
                ("XFTA", "DI", "Fault alarm"),
                ("SC", "AO", "Speed control signal (%)"),
                ("SI", "AI", "Speed feedback signal (%)"),
                ("XOLA", "DI", "Overload detected")
            ]
        },
        {
            "description": "Basic Conveyor Belt",
            "suffixes": [
                ("XFWD", "DO", "Forward start command"),
                ("XREV", "DO", "Reverse start command"),
                ("XSTP", "DO", "Stop command"),
                ("XFWF", "DI", "Forward running feedback"),
                ("XRVF", "DI", "Reverse running feedback"),
                ("XFTA", "DI", "Fault alarm")
            ]
        }
    ]
}

# Process units define logical groupings of devices that interact with each other
PROCESS_UNITS = {
    "PUMP_STATION": {
        "description": "Pump station with flow and pressure monitoring",
        "devices": [
            {"type": "PM", "count": 1, "required": True},   # Pump motor
            {"type": "FT", "count": 1, "required": True},   # Flow transmitter to monitor pump output
            {"type": "PT", "count": 1, "required": True},   # Pressure transmitter on discharge line
            {"type": "VC", "count": 1, "required": False},  # Optional valve
        ]
    },
    "TANK_SYSTEM": {
        "description": "Storage tank with level monitoring",
        "devices": [
            {"type": "LT", "count": 1, "required": True},   # Level transmitter
            {"type": "TT", "count": 1, "required": False},  # Optional temperature sensor
            {"type": "VC", "count": 2, "required": False},  # Optional inlet/outlet valves
        ]
    },
    "TRANSFER_SYSTEM": {
        "description": "Product transfer system",
        "devices": [
            {"type": "PM", "count": 1, "required": True},   # Pump motor
            {"type": "FT", "count": 1, "required": True},   # Flow transmitter
            {"type": "VC", "count": 2, "required": True},   # Inlet/outlet valves
        ]
    },
    "COMPRESSOR_UNIT": {
        "description": "Compressor with pressure and temperature monitoring",
        "devices": [
            {"type": "CA", "count": 1, "required": True},   # Compressor
            {"type": "PT", "count": 2, "required": True},   # Inlet/outlet pressure transmitters
            {"type": "TT", "count": 1, "required": True},   # Temperature monitoring
        ]
    },
    "VENTILATION_SYSTEM": {
        "description": "Ventilation system with temperature control",
        "devices": [
            {"type": "FN", "count": 1, "required": True},   # Fan starter
            {"type": "TT", "count": 1, "required": True},   # Temperature sensor
        ]
    },
    "MIXING_SYSTEM": {
        "description": "Product mixing system with temperature control",
        "devices": [
            {"type": "MX", "count": 1, "required": True},   # Mixer
            {"type": "TT", "count": 1, "required": True},   # Temperature sensor
            {"type": "LT", "count": 1, "required": True},   # Level transmitter
            {"type": "VC", "count": 2, "required": False},  # Optional valves
        ]
    },
    "HEATING_SYSTEM": {
        "description": "Product heating system",
        "devices": [
            {"type": "HTR", "count": 1, "required": True},  # Heater
            {"type": "TT", "count": 2, "required": True},   # Temperature sensors (inlet/outlet)
            {"type": "FT", "count": 1, "required": False},  # Optional flow transmitter
        ]
    },
    "VFD_PUMP_SYSTEM": {
        "description": "Variable speed pump system",
        "devices": [
            {"type": "VFD", "count": 1, "required": True},  # Variable frequency drive
            {"type": "FT", "count": 1, "required": True},   # Flow transmitter
            {"type": "PT", "count": 1, "required": True},   # Pressure transmitter
        ]
    },
    "BATCHING_SYSTEM": {
        "description": "Batch weighing and dosing system",
        "devices": [
            {"type": "VC3", "count": 2, "required": True},  # Three-position valves for dosing
            {"type": "MX", "count": 1, "required": False},  # Optional mixer
        ]
    },
    "MATERIAL_HANDLING": {
        "description": "Material handling system with conveyor belt",
        "devices": [
            {"type": "CB", "count": 1, "required": True},   # Conveyor belt
            {"type": "VC", "count": 1, "required": False},  # Optional discharge valve
            {"type": "FT", "count": 1, "required": False},  # Optional flow monitoring
            {"type": "LT", "count": 2, "required": False},  # Optional level sensors (input/output)
        ]
    },
    "PACKAGING_LINE": {
        "description": "Product packaging line with conveyor and sensors",
        "devices": [
            {"type": "CB", "count": 2, "required": True},   # Multiple conveyor belts
            {"type": "PT", "count": 1, "required": False},  # Optional pressure sensor
            {"type": "FT", "count": 1, "required": False},  # Optional flow sensor
        ]
    }
}

DEVICE_DEFINITIONS = {
    "LT": {
        "description": "Level Sensor",
        "suffixes": [
            ("LI", "AI", "Liquid level indicator")
        ]
    },
    "FT": {
        "description": "Flow Sensor",
        "suffixes": [
            ("FI", "AI", "Flow volume indication")
        ]
    },
    "TT": {
        "description": "Temperature Sensor",
        "suffixes": [
            ("TI", "AI", "Process temperature value")
        ]
    },
    "PT": {
        "description": "Pressure Sensor",
        "suffixes": [
            ("PI", "AI", "Process pressure value")
        ]
    },
    "PM": [
        {
            "description": "Pump Drive Controller Type A",
            "suffixes": [
                ("XST", "DO", "Activate pump operation"),
                ("XSP", "DO", "Deactivate pump operation"),
                ("XRC", "DO", "Enable external control"),
                ("XRN", "DI", "Pump operation status"),
                ("XPFA", "DI", "Electrical supply fault"),
                ("XOLA", "DI", "Excessive load detected")
            ]
        },
        {
            "description": "Pump Drive Controller Type B",
            "suffixes": [
                ("XST", "DO", "Initiate pump operation"),
                ("XSP", "DO", "Terminate pump operation"),
                ("XRS", "DO", "Clear fault condition"),
                ("XRN", "DI", "Operation status indicator"),
                ("XHFA", "DI", "Excessive flow detected"),
                ("XOLA", "DI", "Motor load threshold exceeded")
            ]
        },
        {
            "description": "Pump Drive Controller Type C",
            "suffixes": [
                ("XST", "DO", "Initiate motor rotation"),
                ("XSP", "DO", "Cease motor rotation"),
                ("XRC", "DO", "Activate remote operation"),
                ("XRN", "DI", "Motor operational status"),
                ("XHTA", "DI", "Excessive temperature warning"),
                ("XOLA", "DI", "Motor protection activated")
            ]
        }
    ],
    "VC": {
        "description": "Valve Controller",
        "suffixes": [
            ("XOC", "DO", "Actuate valve opening"),
            ("XCC", "DO", "Actuate valve closing"),
            ("XOF", "DI", "Open position confirmation"),
            ("XCF", "DI", "Closed position confirmation")
        ]
    },
    "VC3": {
        "description": "Three-State Valve Controller",
        "suffixes": [
            ("XOC", "DO", "Open valve"),
            ("XCC", "DO", "Close valve"),
            ("XIC", "DO", "Move to middle position"),
            ("XOF", "DI", "Status: completely open"),
            ("XCF", "DI", "Status: completely closed"),
            ("XIF", "DI", "Status: partially opened"),
            ("XMV", "DI", "Status: in transition"),
            ("XFT", "DI", "Controller malfunction"),
            ("POS", "AI", "Position measurement (0-100%)"),
            ("XRS", "DO", "Clear fault condition")
        ]
    },
    "FN": {
        "description": "Fan Controller",
        "suffixes": [
            ("XST", "DO", "Activate fan rotation"),
            ("XSP", "DO", "Deactivate fan rotation"),
            ("XRN", "DI", "Fan operational status")
        ]
    },
    "CA": {
        "description": "Compression Unit Controller",
        "suffixes": [
            ("XST", "DO", "Initiate compression"),
            ("XSP", "DO", "Terminate compression"),
            ("XRN", "DI", "Compression active status"),
            ("XPFA", "DI", "Electrical fault detected")
        ]
    },
    "VFD": [
        {
            "description": "Speed Controller Standard",
            "suffixes": [
                ("XST", "DO", "Activate drive"),
                ("XSP", "DO", "Deactivate drive"),
                ("XRS", "DO", "Clear error state"),
                ("XRN", "DI", "Drive operational status"),
                ("XFT", "DI", "Error condition present"),
                ("SC", "AO", "Rotation speed setpoint"),
                ("SI", "AI", "Actual rotation speed")
            ]
        },
        {
            "description": "Speed Controller Enhanced",
            "suffixes": [
                ("XST", "DO", "Initiate drive operation"),
                ("XSP", "DO", "Cease drive operation"),
                ("XRS", "DO", "Reset error condition"),
                ("XRC", "DO", "Activate external control"),
                ("XRN", "DI", "Status: drive active"),
                ("XFT", "DI", "Status: error detected"),
                ("SC", "AO", "Speed reference value"),
                ("SI", "AI", "Measured speed value"),
                ("CI", "AI", "Electrical current value"),
                ("XMA", "DI", "Local operation enabled")
            ]
        }
    ],
    "HTR": [
        {
            "description": "Heating Element Basic",
            "suffixes": [
                ("XST", "DO", "Activate heating"),
                ("XRN", "DI", "Heating active status")
            ]
        },
        {
            "description": "Heating Element Advanced",
            "suffixes": [
                ("XST", "DO", "Initiate heating process"),
                ("XSP", "DO", "Terminate heating process"),
                ("XRN", "DI", "Heat generation status"),
                ("TC", "AO", "Temperature setpoint"),
                ("TI", "AI", "Measured temperature")
            ]
        }
    ],
    "MX": [
        {
            "description": "Agitation Unit Basic",
            "suffixes": [
                ("XST", "DO", "Activate agitation"),
                ("XRN", "DI", "Agitation active status"),
                ("XOLA", "DI", "Excessive load warning")
            ]
        },
        {
            "description": "Agitation Unit Advanced",
            "suffixes": [
                ("XST", "DO", "Initiate material mixing"),
                ("XSP", "DO", "Terminate material mixing"),
                ("XRN", "DI", "Status: mixing active"),
                ("XOLA", "DI", "Warning: excessive load"),
                ("SC", "AO", "Rotation speed setpoint"),
                ("TI", "AI", "Process temperature value")
            ]
        }
    ],
    "CB": [
        {
            "description": "Material Transport System",
            "suffixes": [
                ("XFWD", "DO", "Initiate forward movement"),
                ("XREV", "DO", "Initiate reverse movement"),
                ("XSTP", "DO", "Halt all movement"),
                ("XFWF", "DI", "Status: moving forward"),
                ("XRVF", "DI", "Status: moving backward"),
                ("XRDY", "DI", "System operational"),
                ("XFTA", "DI", "System malfunction"),
                ("SC", "AO", "Movement rate setpoint (%)"),
                ("SI", "AI", "Measured movement rate (%)"),
                ("XOLA", "DI", "Excessive load detected")
            ]
        },
        {
            "description": "Simple Transport System",
            "suffixes": [
                ("XFWD", "DO", "Activate forward motion"),
                ("XREV", "DO", "Activate reverse motion"),
                ("XSTP", "DO", "Cease all motion"),
                ("XFWF", "DI", "Forward motion active"),
                ("XRVF", "DI", "Reverse motion active"),
                ("XFTA", "DI", "System fault indicator")
            ]
        }
    ]
}

# Process units define logical groupings of devices that interact with each other
PROCESS_UNITS = {
    "PUMP_STATION": {
        "description": "Fluid transfer station with measurement capabilities",
        "devices": [
            {"type": "PM", "count": 1, "required": True},   # Pump controller
            {"type": "FT", "count": 1, "required": True},   # Flow measurement device
            {"type": "PT", "count": 1, "required": True},   # Outlet pressure sensor
            {"type": "VC", "count": 1, "required": False},  # Optional flow control valve
        ]
    },
    "TANK_SYSTEM": {
        "description": "Fluid containment system with monitoring",
        "devices": [
            {"type": "LT", "count": 1, "required": True},   # Content level monitor
            {"type": "TT", "count": 1, "required": False},  # Optional content temperature monitor
            {"type": "VC", "count": 2, "required": False},  # Optional inlet/outlet flow controllers
        ]
    },
    "TRANSFER_SYSTEM": {
        "description": "Material conveyance configuration",
        "devices": [
            {"type": "PM", "count": 1, "required": True},   # Transport drive
            {"type": "FT", "count": 1, "required": True},   # Material flow sensor
            {"type": "VC", "count": 2, "required": True},   # Flow control devices
        ]
    },
    "COMPRESSOR_UNIT": {
        "description": "Gas compression system with parameter monitoring",
        "devices": [
            {"type": "CA", "count": 1, "required": True},   # Compression device
            {"type": "PT", "count": 2, "required": True},   # Entry/exit pressure monitors
            {"type": "TT", "count": 1, "required": True},   # Process temperature monitor
        ]
    },
    "VENTILATION_SYSTEM": {
        "description": "Air circulation system with climate regulation",
        "devices": [
            {"type": "FN", "count": 1, "required": True},   # Air movement device
            {"type": "TT", "count": 1, "required": True},   # Air temperature monitor
        ]
    },
    "MIXING_SYSTEM": {
        "description": "Material blending station with condition monitoring",
        "devices": [
            {"type": "MX", "count": 1, "required": True},   # Blending mechanism
            {"type": "TT", "count": 1, "required": True},   # Process temperature monitor
            {"type": "LT", "count": 1, "required": True},   # Material quantity monitor
            {"type": "VC", "count": 2, "required": False},  # Optional material flow controllers
        ]
    },
    "HEATING_SYSTEM": {
        "description": "Thermal regulation assembly",
        "devices": [
            {"type": "HTR", "count": 1, "required": True},  # Thermal element
            {"type": "TT", "count": 2, "required": True},   # Entry/exit temperature monitors
            {"type": "FT", "count": 1, "required": False},  # Optional flow rate monitor
        ]
    },
    "VFD_PUMP_SYSTEM": {
        "description": "Adjustable-rate fluid transfer assembly",
        "devices": [
            {"type": "VFD", "count": 1, "required": True},  # Rate control mechanism
            {"type": "FT", "count": 1, "required": True},   # Flow measurement device
            {"type": "PT", "count": 1, "required": True},   # Pressure measurement device
        ]
    },
    "BATCHING_SYSTEM": {
        "description": "Precise material portioning configuration",
        "devices": [
            {"type": "VC3", "count": 2, "required": True},  # Multi-position material flow controllers
            {"type": "MX", "count": 1, "required": False},  # Optional material homogenizer
        ]
    },
    "MATERIAL_HANDLING": {
        "description": "Bulk material transport configuration",
        "devices": [
            {"type": "CB", "count": 1, "required": True},   # Continuous transport mechanism
            {"type": "VC", "count": 1, "required": False},  # Optional output flow controller
            {"type": "FT", "count": 1, "required": False},  # Optional material movement monitor
            {"type": "LT", "count": 2, "required": False},  # Optional material presence monitors
        ]
    },
    "PACKAGING_LINE": {
        "description": "Product enclosure and preparation station",
        "devices": [
            {"type": "CB", "count": 2, "required": True},   # Sequential transport mechanisms
            {"type": "PT", "count": 1, "required": False},  # Optional compression monitor
            {"type": "FT", "count": 1, "required": False},  # Optional production rate monitor
        ]
    }
}

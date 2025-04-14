# IO List Processor

A tool for generating realistic I/O (Input/Output) lists for industrial control systems.

## Overview

This application generates realistic I/O points that might be found in an industrial automation project. It creates a variety of device types, including:

- Level transmitters
- Flow transmitters
- Temperature sensors
- Pump motor starters
- Valve actuators
- And more...

## Features

- Generate complete I/O lists with realistic tagnames
- Create logical groupings of devices into process units
- Output as CSV or Excel files
- Configurable number of I/O points to generate

## Installation

1. Clone this repository
2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Run the generator with default settings:

```
python main.py
```

This will create CSV and Excel files in the `output` directory.

## Project Structure

- `src/` - Source code
  - `config/` - Configuration settings and device definitions
  - `generators/` - I/O list generation logic
  - `utils/` - Helper utilities for file output
- `tests/` - Unit tests
- `output/` - Generated I/O lists (created when running)

## Configuration

You can customize the generation process by modifying files in the `src/config/` directory:

- `constants.py` - Basic settings like number of rows
- `device_definitions.py` - Device types and their signal configurations

## Testing

Run the unit tests with:

```
python -m unittest discover -s tests
```


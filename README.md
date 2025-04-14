# IO-AutoMapper 

A tool for to map IO signal list entries to control library function blocks.

## Features

- Takes Excel IO lists as input
- Process the IO list entries in smaller chunks and maps them to predefined function blocks
- Output: an Excel IO list with additional columns specifying the mapping

## Installation

1. Clone this repository
2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Modify src/config/defaults.py with the desired configuration parmameters.
Then run

```
python io-automapper.py
```

This will create an Excel file.

## Project Structure

- `src/` - Source code
  - `config/` - Configuration settings 
  - `core/` - Mapping procedures 
  - `utils/` - Excel and AI utilities
- `test-data/` - Testing data

## License

[Apache 2.0](LICENSE)
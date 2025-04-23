# IO-AutoMapper 

A tool to map IO signal list entries to control library function blocks. Details of the tool are described in a paper submitted to IEEE ETFA 2025.

## Features

- Takes an Excel IO list as input
- Processes the IO list entries in smaller chunks and maps them to predefined function blocks
- Output: an Excel IO list with additional columns specifying the mapping

## Installation and Usage

1. Clone this repository
2. Install dependencies:
```
pip install -r requirements.txt
```

Modify the file ".env" and enter your own LLM API endpoint and key. If you are not using AzureOpenAI, also modifiy src/utils/ai_utils.py and configure your favorite LLM.

Modify src/config/defaults.py with the desired configuration parameters. 
You can also try one of three pre-defined configurations, which point to the generated IO lists in the folder test-data.

To process a new kind of IO list, you can create a new configuration. You need to specify the filename, the columns and rows to process, and the desired tagname pattern with device prefix and signal suffix.
If you do not have a ground truth IO list with the correct mapping, then disable the ground truth check by setting ENABLE_GROUND_TRUTH_CHECK = False in defaults.py.

Then run

```
python io-automapper.py
```

This will process the input Excel file and issues a series of prompts against the configured LLM.
In our tests, processing 300 signals currently took about 30 minutes. You can configure a smaller row range to limit the time duration.
The output of this process will be a new Excel file with three additional columns that specify the mapping of the IO list entries to function blocks and their parameters.
If the ground truth check is enabled, you will also receive a short report indicating the correct and incorrect mappings.

## Project Structure

- `src/` - Source code
  - `config/` - Configuration settings 
  - `core/` - Mapping procedures 
  - `utils/` - Excel and AI utilities
- `test-data/` - Testing data
- `prompt_templates_LIB1` - Prompts for mapping to the conceptual control library LIB1
- `io_list_generation` - IO list generator to sythesize random IO lists as test data

## License

[Apache 2.0](LICENSE)
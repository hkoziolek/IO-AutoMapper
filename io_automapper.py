from datetime import datetime, timezone
from dotenv import load_dotenv
import os
import sys

# Add the parent directory to the Python path to allow importing from src
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Load environment variables
load_dotenv()

# Import custom modules from src
from src.config.defaults import DEFAULT_CONFIG, ALTERNATIVE_CONFIGS, PROMPT_TEMPLATES_DIR, ENABLE_GROUND_TRUTH_CHECK
from src.utils.ai_utils import initialize_llm, print_token_statistics
from src.utils.excel_utils import extract_lines_from_excel, check_ground_truth_mismatches2, save_output_to_excel
from src.core.device_mapper import identify_devices
from src.core.function_block_mapper import map_devices_to_function_blocks

def main(config):
    """Main execution function."""
    start_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"Start time: {start_time}")

    # Initialize the LLM
    llm = initialize_llm()
    
    # Extract data from Excel
    headers, extracted_rows = extract_lines_from_excel(
        config["file"], 
        config["columns"],
        config["start_line"], 
        config["end_line"]
    )
    
    # Identify device candidates
    json_data = identify_devices(
        llm,
        PROMPT_TEMPLATES_DIR,
        headers, 
        extracted_rows,
        config["signal_tag_column"],
        config["tagname_pattern"]
    )
    
    # Map devices to function blocks
    out_df = map_devices_to_function_blocks(
        llm,
        PROMPT_TEMPLATES_DIR,
        extracted_rows, 
        json_data
    )

    # Save results
    print(f"\nProcessing I/O list done (Row {config['start_line']}-{config['end_line']}).")
    output_file = save_output_to_excel(out_df, config["file"])
    
    # Optional ground truth check
    if ENABLE_GROUND_TRUTH_CHECK:
        import pandas as pd

        base_filename = config["file"].split(".")[0] + "_output"
        filename = base_filename + ".xlsx"
        counter = 1
        while os.path.exists(filename):
            filename = f"{base_filename}{counter}.xlsx"
            counter += 1
        filename = f"{base_filename}{counter-2}.xlsx"

        ground_truth_check_result_file = filename[:-5] + "_check.txt"

        ground_truth_file = config["file"][:-5] + "_ground_truth.xlsx"
        data = pd.read_excel(ground_truth_file)
        extracted_rows = data.iloc[config["start_line"]-1:config["end_line"]]
        check_ground_truth_mismatches2(extracted_rows, out_df, ground_truth_check_result_file, config["columns"][0])

    # Print timing information
    stop_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"Stop time: {stop_time}")
    duration = datetime.strptime(stop_time, "%Y-%m-%dT%H:%M:%SZ") - datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    duration_str = f"{int(hours)}:{int(minutes):02}:{int(seconds):02}"
    print(f"Duration: {duration_str}")

if __name__ == "__main__":
    main(ALTERNATIVE_CONFIGS["DEVLIST1"])

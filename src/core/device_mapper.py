import json
import re
from src.utils.ai_utils import prompt_llm, convert_formatted_JSON_code_block_to_raw_JSON

def identify_devices(llm, prompt_templates_dir, headers, extracted_rows, signal_tag_column, tagname_pattern):
    """Identify devices from IO list rows."""
    # Remove commas within fields to avoid breaking the CSV format
    for index, row in extracted_rows.iterrows():
        for col in extracted_rows.columns:
            if isinstance(row[col], str):
                extracted_rows.at[index, col] = row[col].replace(',', '')

    # Prefix lines with line numbers
    all_rows = []
    for index, row in extracted_rows.iterrows():
        content = ', '.join(map(str, row.tolist()))
        all_rows.append(f"{index+2}: {content}\n")

    print("\nStep 1: Identify candidate devices for function block mapping.")
    
    response = "[]"
    max_number_of_rows = len(all_rows)
    next_start_row = 0
    
    while next_start_row < max_number_of_rows:
        # Get next chunk of 20 rows
        if next_start_row + 20 < max_number_of_rows:
            next_end_row = next_start_row + 20
        else:
            next_end_row = max_number_of_rows
        chunk = all_rows[next_start_row:next_end_row]

        # Create a chunk of data with the same tagname prefix (e.g., 100-XY100) 
        chunk_index = 0 
        target_signal_tag_prefix = ""
        
        for entry in chunk:
            parts = entry.split(',')
            signal_tag = parts[signal_tag_column].strip()
            
            if signal_tag_column == 0: # account for the line number
                signal_tag = signal_tag.split(':',1)[1].strip()
            signal_tag = signal_tag.replace(" ", "") # remove any blanks from signal_tag
            
            prefix = ""
            match_tagname_pattern = tagname_pattern.match(signal_tag)
            if match_tagname_pattern:
                prefix = match_tagname_pattern.group("prefix")
            else:
                print(f"Signal tag '{signal_tag}' does not match the expected pattern.")
                exit()
            if target_signal_tag_prefix == "": # first iteration
                target_signal_tag_prefix = prefix
            if prefix != target_signal_tag_prefix:
                break
            chunk_index += 1
        chunk = chunk[0:chunk_index]

        # Process the reduced chunk
        first_item = chunk[0].split(':', 1)[0].strip()
        last_item = chunk[-1].split(':', 1)[0].strip()
        print(f"Row {first_item}-{last_item}")
        
        mute = True
        reduced_data = prompt_llm(llm, "", chunk, f"{prompt_templates_dir}/identify_devices_task1.txt", is_muted=mute)
        classified_data = prompt_llm(llm, "", reduced_data, f"{prompt_templates_dir}/identify_devices_task2.txt", is_muted=mute) 
        keyword_data = prompt_llm(llm, "", classified_data, f"{prompt_templates_dir}/identify_devices_task3.txt", is_muted=mute)
        qualified_data = prompt_llm(llm, "", keyword_data, f"{prompt_templates_dir}/identify_devices_task4.txt", is_muted=mute)
        row_to_device_mapping = prompt_llm(llm, "", qualified_data, f"{prompt_templates_dir}/identify_devices_task5.txt", is_muted=mute)
        final_row_to_device_mapping = prompt_llm(llm, row_to_device_mapping, qualified_data, f"{prompt_templates_dir}/identify_devices_task6.txt", is_muted=mute)

        response_data = json.loads(response) # convert JSON to Python list
        final_mapping_data = json.loads(convert_formatted_JSON_code_block_to_raw_JSON(final_row_to_device_mapping)) # convert JSON to Python list
        response_data.extend(final_mapping_data)
        response = json.dumps(response_data, indent=2) # convert Python list back to JSON string

        next_start_row = next_start_row + chunk_index

    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        return []
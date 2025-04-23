from src.utils.ai_utils import prompt_llm

def map_devices_to_function_blocks(llm, prompt_templates_dir, extracted_rows, json_data):
    """Map identified devices to function blocks."""
    print("\nStep 2: Map candidate devices to function blocks.")
    out_df = extracted_rows.copy()
    out_df.insert(0,"Line", out_df.index+2)
    out_df["Signal Data Type"] = ""
    out_df["Function Block Type"] = ""
    out_df["Function Block Parameter"] = ""

    header = ["Line"]
    header.extend(extracted_rows.columns.tolist())
    header.extend(["Signal Data Type", "Function Block Type", "Function Block Parameter"])

    for entry in json_data:
        start_row = entry["startRow"]
        end_row = entry["endRow"]
        tagname = entry["tag"]

        if start_row != end_row:
            # This is a device with multiple signals
            print(f"{tagname} -> ")
            df_filtered = out_df[(out_df["Line"]>=start_row) & (out_df["Line"]<=end_row)]
            selected_rows = []
            for index, row in df_filtered.iterrows():
                content = ', '.join(map(str, row.tolist()))
                selected_rows.append(f"{content}\n")
            cb_object_name = prompt_llm(llm, header, selected_rows, f"{prompt_templates_dir}/map_devices_to_function_blocks.txt", is_muted=False)
            
            # Map each signal of the device to a function block parameter
            for index, row in df_filtered.iterrows():
                row_content = ', '.join(map(str, row.tolist()))

                out_df.at[index, "Function Block Type"] = cb_object_name
                
                # Determine the Signal Data Type
                signal_type = prompt_llm(llm, header, row_content, f"{prompt_templates_dir}/get_cb_object_type2.txt", is_muted=True)
                out_df.at[index, "Signal Data Type"] = signal_type

                # Determine the function block parameter
                cb_object_parameter = prompt_llm(llm, header, row_content, f"{prompt_templates_dir}/map_parameters_"+cb_object_name.lower()+".txt", is_muted=True)
                out_df.at[index, "Function Block Parameter"] = cb_object_parameter
        else:
            # Map individual signals
            matching_row = out_df[out_df["Line"]==start_row]
            row_content = ', '.join(map(str, matching_row.values.tolist()))            
            signal_type = prompt_llm(llm, header, row_content, f"{prompt_templates_dir}/get_cb_object_type1.txt", is_muted=True)
            out_df.loc[out_df["Line"]==start_row, "Signal Data Type"] = signal_type

    return out_df

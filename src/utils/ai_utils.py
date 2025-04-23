from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage
from langsmith import Client
import time
from datetime import datetime, timezone

def initialize_llm():
    """Initialize and configure the LLM."""
    return AzureChatOpenAI(
        openai_api_version="TODO",
        model="TODO",
        azure_deployment="TODO",
        azure_endpoint="TODO",
        streaming=True,
        verbose=True,
        temperature=0.0,
    )

def load_prompt_from_file(filepath):
    """Load a prompt template from a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found: {filepath}")
    except Exception as e:
        raise Exception(f"Error reading prompt file: {e}")

def prompt_llm(llm, header, data, prompt_file, is_muted=False, max_retries=10):
    """Send a prompt to the LLM and get the response. Retry up to max_retries times if an exception occurs."""
    prompt_template = load_prompt_from_file(prompt_file)
    formatted_prompt = prompt_template.format(header=header, content=data)
    message = HumanMessage(content=formatted_prompt)
    
    retry_count = 0
    while retry_count <= max_retries:
        try:
            # Stream LLM response
            response_content = ""
            dot_counter = 0  # Counter to track chunks for muted output
            prompt_name = prompt_file.split("/")[-1][:-4]
            
            if retry_count > 0:
                print(f"{prompt_name} (Attempt {retry_count+1}/{max_retries+1}): ", end="", flush=True)
            else:
                print(f"{prompt_name}: ", end="", flush=True)
            
            for chunk in llm.stream([message]): 
                chunk_text = chunk.content
                if chunk_text:  # Check if chunk has content
                    if (is_muted):
                        dot_counter += 1
                        # Print the counter and then a carriage return to overwrite the previous number
                        print(f"\r{prompt_name}: {dot_counter}", end="", flush=True)
                    else:
                        print(chunk_text, end="", flush=True)  
                    response_content += chunk_text 

            # Print a newline after completion
            print() 
           
            return response_content
            
        except Exception as e:
            retry_count += 1
            if retry_count <= max_retries:
                # Exponential backoff: wait longer with each retry
                wait_time = 2 ** retry_count
                print(f"Error on attempt {retry_count}: {e}")
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Failed after {max_retries} retries. Last error: {e}")
                return f"Error generating LLM response after {max_retries} retries: {e}"

def convert_formatted_JSON_code_block_to_raw_JSON(str):
    """Convert a JSON code block to raw JSON."""
    if (str.startswith("```")):
        str = str[7:]
        str = str[:-3]
    return str
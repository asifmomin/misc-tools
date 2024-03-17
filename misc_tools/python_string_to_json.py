import sys
import ast
import json
import pyperclip


def parse_nested_json(data):
    if isinstance(data, str):
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return data
    elif isinstance(data, dict):
        return {k: parse_nested_json(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [parse_nested_json(item) for item in data]
    else:
        return data


# Check if the filename is provided
if len(sys.argv) < 2:
    print("Please provide a filename as a command line argument.")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        data_str = file.read()

    data_dict = ast.literal_eval(data_str)
    data_dict = parse_nested_json(data_dict)


    json_string = json.dumps(data_dict, indent=4)
    event_text = data_dict.get('body', {}).get('event', {}).get('text', '')

    print(json_string)
    pyperclip.copy(event_text)
    
    # ANSI escape code for green text
    green_text = '\033[92m'
    reset_text = '\033[0m'
    print(f"{green_text}JSON string copied to clipboard.{reset_text}")




except FileNotFoundError:
    print(f"File not found: {filename}")
except ValueError as e:
    print(f"Error processing file: {e}")

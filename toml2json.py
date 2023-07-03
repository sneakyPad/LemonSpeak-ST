import toml
import json



def parse_firestore_toml_to_json():
    # Load TOML file
    toml_file = ".streamlit/secrets.toml"
    with open(toml_file, "r") as file:
        toml_content = toml.load(file)

    # Extract the Python dictionary stored under the 'textkey' key
    json_dict = toml_content.get('firestore', {})

    # Convert the Python dictionary to a JSON string
    json_content = json.dumps(json_dict)

    # If you want to write this JSON string to a new JSON file
    output_json_file = ".streamlit/fs_key.json"

    with open(output_json_file, 'w') as json_file:
        json_file.write(json_content)
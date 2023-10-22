import json

# Define the path to the info.json file
info_json_path = 'info.json'

try:
    with open(info_json_path, 'r') as file:
        data = json.load(file)

    if data:
        print("Data found in info.json:")
        for entry in data:
            print("Username:", entry['username'])
            print("Room ID:", entry['room_id'])
            print()
    else:
        print("No data found in info.json.")
except FileNotFoundError:
    print("The info.json file does not exist.")
except json.JSONDecodeError:
    print("The info.json file is not in valid JSON format.")

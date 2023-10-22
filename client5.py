from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['post'])
def handle_request():
    try:
        data = request.get_json()
        if 'username' in data and 'room_id' in data:
            username = data['username']
            room_id = data['room_id']
            
            # Create a dictionary to store request data
            request_data = {
                'username': username,
                'room_id': room_id,
            }
            
            # Load existing data from info.json if it exists
            try:
                with open('info.json', 'r') as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Append the new request data
            existing_data.append(request_data)

            # Save the updated data to info.json
            with open('info.json', 'w') as file:
                json.dump(existing_data, file, indent=2)

            print(f"Received a POST request with username: {username} and room ID: {room_id}")
            return "Request received"
        else:
            return "Bad request. Please provide 'username' and 'room_id' in the JSON data.", 400
    except Exception as e:
        return f"Bad request. Error: {str(e)}", 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)



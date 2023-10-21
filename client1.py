

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])

def handle_request():
    if request.method == 'GET' :
        print("Received request")
    
    return "Request received"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000) 

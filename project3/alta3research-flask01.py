#!/usr/bin/env python3

"""
This is a simple Flask API script that demonstrates creating a basic RESTful API.

The API has two endpoints:
1. '/json-data': This endpoint returns JSON data, representing a list of people with their names and ages.
2. '/protected-data': This endpoint requires a session value (authentication) to access and returns a message.

The API is hosted on 'http://localhost:5000/' (your local machine). since this is a proof of concept lab.

To test this script, you can use the 'alta3research-requests02.py' script to send requests to this API.

Prerequisites:
- Python 3 and Flask library installed.
"""

from flask import Flask, jsonify, request, session

app = Flask(__name__)

# Sample data in a list of dictionaries
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]

# Endpoint to return JSON data
@app.route('/json-data', methods=['GET'])
def get_json_data():
    return jsonify(data)

# Endpoint that requires a session value to get a response
@app.route('/protected-data', methods=['GET'])
def get_protected_data():
    # Check if 'authenticated' key is present in the session
    if 'authenticated' in session:
        return "You have access to protected data!"
    else:
        return "Authentication required!", 401

if __name__ == '__main__':
    app.run(debug=True)


#!/usr/bin/env python3

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


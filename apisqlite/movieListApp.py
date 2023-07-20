#!/usr/bin/env python3
"""Eric Phelps Flask app to contain movie DB for challenge lab 113"""
from flask import Flask, request, jsonify
import sqlite3
from apisqlite01 import movielookup, movielookup_by_year, movielookup_by_type_and_year, print_local_db

app = Flask(__name__)


# Flask routes
@app.route('/')
def index():
    return "Welcome to the OMDB Movie Client and DB API!"

@app.route('/search', methods=['GET'])
def search_movies():
    searchstring = request.args.get('searchstring')
    movietype = request.args.get('type')
    year = request.args.get('year')

    # Check if a searchstring is provided
    if not searchstring:
        return jsonify({'error': 'No search string provided.'}), 400

    # Implement the search logic using the API functions
    mykey = "your_omdb_api_key"  # Replace this with your actual OMDB API key

    if movietype and year:
        results = movielookup_by_type_and_year(mykey, searchstring, movietype, year)
    elif movietype:
        results = movielookup_by_type(mykey, searchstring, movietype)
    elif year:
        results = movielookup_by_year(mykey, searchstring, year)
    else:
        results = movielookup(mykey, searchstring)

    if results:
        return jsonify({'message': 'Search results', 'data': results}), 200
    else:
        return jsonify({'message': 'No results found for the search.'}), 404

@app.route('/localdb', methods=['GET'])
def get_local_db():
    try:
        conn = sqlite3.connect('mymovie.db')
        cursor = conn.execute("SELECT * from MOVIES")
        movies = [{'title': row[0], 'year': row[1]} for row in cursor]
        conn.close()

        if movies:
            return jsonify({'message': 'Local database contents', 'data': movies}), 200
        else:
            return jsonify({'message': 'The local database is empty.'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving data from the database.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

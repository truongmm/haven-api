from app import app
from flask import jsonify
from session import Session

# Initialize Session
session = Session()

# Home Request
@app.route('/')
def main():
  return 'Haven API by Linked Ladies'

# GET Requests
@app.route('/api/disasters', methods=['GET'])
def get_disasters():
  return jsonify({'disasters': session.getDisasters()})

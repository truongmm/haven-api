from app import app
from flask import jsonify, request
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

@app.route('/api/shelters', methods=['GET'])
def get_shelters():
  return jsonify({'shelters': session.getShelters()})

# POST Requests
@app.route('/api/disasters/checkin', methods=['POST'])
def check_in():
  id = request.json['id']
  checkins = request.json['checkins']
  injured = request.json['injured']
  return jsonify({'disasters': session.updateDisaster(id, checkins, injured)})

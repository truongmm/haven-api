from app import db

class Disasters(db.Model):
  __tablename__ = 'disasters'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(45))
  lat = db.Column(db.Float)
  long = db.Column(db.Float)
  totalCheckIns = db.Column(db.Integer)
  totalInjured = db.Column(db.Integer)
  totalChildren = db.Column(db.Integer)
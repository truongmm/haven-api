from app import db
from models import Disasters, Shelters

class Session:
  def formatLocation(self, result):
    return {
      'id': result.id,
      'name': result.name,
      'lat': result.lat,
      'long': result.long,
      'totalCheckIns': result.totalCheckIns,
      'totalInjured': result.totalInjured
    }

  def getDisasters(self):
    results = Disasters.query.all()
    disasters = []
    for result in results:
      disasters.append(self.formatLocation(result))
    return disasters

  def getShelters(self):
    results = Shelters.query.all()
    shelters = []
    for result in results:
      shelters.append(self.formatLocation(result))
    return shelters

  def updateDisaster(self, id, checkins, injured):
    disaster = Disasters.query.get(id)
    disaster.totalCheckIns = disaster.totalCheckIns + checkins
    disaster.totalInjured = disaster.totalInjured + injured
    db.session.commit()
    return self.formatLocation(disaster)
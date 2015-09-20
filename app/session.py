from models import Disasters, Shelters

class Session:
  def formatLocation(self, result):
    return {
      'id': result.id,
      'name': result.name,
      'lat': result.lat,
      'long': result.long,
      'totalCheckIns': result.totalCheckIns,
      'totalInjured': result.totalInjured,
      'totalChildren': result.totalChildren
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
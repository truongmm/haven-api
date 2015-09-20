from models import Disasters

class Session:
  def formatDisaster(self, result):
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
      disasters.append(self.formatDisaster(result))
    return disasters

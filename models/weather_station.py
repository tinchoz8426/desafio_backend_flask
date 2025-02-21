from extensions import db
from geoalchemy2 import Geometry

class WeatherStation(db.Model):
    __tablename__ = 'weather_stations'  # nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(Geometry('POINT', srid=4326), nullable=False)
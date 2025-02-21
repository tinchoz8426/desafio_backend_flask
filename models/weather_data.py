from extensions import db

class WeatherData(db.Model):
    __tablename__ = 'weather_data' # nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey('weather_stations.id', ondelete='CASCADE'), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    pressure = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
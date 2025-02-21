from flask import request, jsonify
from extensions import db
from models.weather_station import WeatherStation
from models.weather_data import WeatherData
from geoalchemy2.functions import ST_Distance, ST_MakePoint, ST_SetSRID
from geoalchemy2.elements import WKTElement

def register_station_routes(app):
    @app.route('/api/stations', methods=['POST'])
    def create_station():
        """
        Creates a new weather station with the provided name and coordinates.

        Expects a JSON payload with the following fields:
        - name: The name of the weather station.
        - latitude: The latitude coordinate of the station.
        - longitude: The longitude coordinate of the station.

        Returns:
        - 400 if any of the required fields are missing or if the coordinates are invalid.
        - 500 if there is an error while creating the station.
        - 201 with the created station's details on successful creation.
        """

        data = request.get_json()
        print(data)
        print(type(data))
        name = data.get('name')
        lat = data.get('latitude')
        lng = data.get('longitude')

        if not all([name, lat, lng]):
            return jsonify({'error': 'Faltan nombre, latitud o longitud'}), 400

        try:
            lat = float(lat)
            lng = float(lng)
        except ValueError:
            return jsonify({'error': 'Latitud o longitud inválidas'}), 400

        point = WKTElement(f'POINT({lng} {lat})', srid=4326)
        new_station = WeatherStation(name=name, location=point)
        
        db.session.add(new_station)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al crear la estación'}), 500

        return jsonify({
            'id': new_station.id,
            'name': new_station.name,
            'latitude': lat,
            'longitude': lng
        }), 201

    @app.route('/api/stations/nearest', methods=['GET'])
    def get_nearest_station():
        lat = request.args.get('lat')
        lng = request.args.get('lng')

        if not all([lat, lng]):
            return jsonify({'error': 'Faltan latitud o longitud'}), 400

        try:
            lat = float(lat)
            lng = float(lng)
        except ValueError:
            return jsonify({'error': 'Latitud o longitud inválidas'}), 400

        ref_point = ST_SetSRID(ST_MakePoint(lng, lat), 4326)
        nearest = WeatherStation.query.order_by(ST_Distance(WeatherStation.location, ref_point)).first()
        
        if not nearest:
            return jsonify({'error': 'No se encontraron estaciones'}), 404

        latest_data = WeatherData.query.filter_by(station_id=nearest.id).order_by(WeatherData.timestamp.desc()).first()

        if not latest_data:
            return jsonify({'error': 'No hay datos para la estación más cercana'}), 404

        return jsonify({
            'name': nearest.name,
            'temperature': latest_data.temperature,
            'humidity': latest_data.humidity,
            'pressure': latest_data.pressure,
            'timestamp': latest_data.timestamp.isoformat()
        }), 200

    @app.route('/api/stations/<int:station_id>', methods=['PUT'])
    def update_station(station_id):
        station = WeatherStation.query.get(station_id)
        print(station)
        
        if not station:
            return jsonify({'error': 'Estación no encontrada'}), 404

        data = request.get_json()
        print(data)
        
        # Verificar campos obligatorios
        required_fields = ['name', 'latitude', 'longitude']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({
                'error': f'Campos obligatorios faltantes: {", ".join(missing_fields)}'
            }), 400

        # Validar coordenadas
        try:
            lat = float(data['latitude'])
            lng = float(data['longitude'])
        except ValueError:
            return jsonify({'error': 'Coordenadas inválidas'}), 400

        # Actualizar datos
        station.name = data['name']
        station.location = WKTElement(f'POINT({lng} {lat})', srid=4326)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al actualizar'}), 500

        return jsonify({'message': 'Estación actualizada'}), 200

    @app.route('/api/stations/<int:station_id>', methods=['DELETE'])
    def delete_station(station_id):
        station = WeatherStation.query.get(station_id)

        if not station:
            return jsonify({'error': 'Estación no encontrada'}), 404

        db.session.delete(station)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al eliminar'}), 500

        return jsonify({'message': 'Estación eliminada'}), 200
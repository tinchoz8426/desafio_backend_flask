from flask import Flask

from extensions import db
from config import Config 
from routes.stations import register_station_routes # importa las rutas

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa la app con la extensión db
db.init_app(app)

# registra las rutas
register_station_routes(app)


if __name__ == '__main__':
    app.run(debug=True)
# 🚀 Desafío Backend Flask

Bienvenido a **Desafío Backend Flask**, un proyecto API REST en Flask con 4 endpoints para gestionar estaciones meteorológicas

## 📌 Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python 3.9.7 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (pip install virtualenv)

## 🔧 Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

```bash
# Clona este repositorio
git clone https://github.com/tinchoz8426/desafio_backend_flask.git
cd desafio_backend_flask

# Crea un entorno virtual (opcional pero recomendado)
python -m venv .venv
source .venv/bin/activate  # En Windows usa: venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt
```

## 🚀 Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
flask run
```

Por defecto, la aplicación se ejecutará en `http://127.0.0.1:5000/`.

## 📁 Estructura del Proyecto

```bash
desafio_backend_flask/
│── models/              # Modelos de datos
│   │── weather_data.py  # Manejo de datos climáticos
│   │── weather_station.py  # Información de estaciones meteorológicas
│── routes/              # Definición de rutas de la API
│   │── stations.py      # Endpoints para estaciones
│── .gitignore           # Archivos a ignorar en Git
│── app.py               # Archivo principal de la aplicación
│── config.py            # Configuración del proyecto
│── extensions.py        # Extensiones y configuraciones adicionales
│── README.md            # Documentación del proyecto
└── requirements.txt     # Dependencias del proyecto
```

## 🛠 Tecnologías Utilizadas

- **Python** 🐍
- **Flask** 🌶️
- **SQLAlchemy** ⚗️
- **GeoAlchemy2** 🌎
- **PostgreSQL** 🐘

## 📡 Endpoints de la API

### 📌 Crear una estación meteorológica
**POST** `http://127.0.0.1:5000/api/stations`

#### 🔹 JSON de ejemplo:
```json
{
  "name": "Parque Patricios",
  "latitude": 95.8786, 
  "longitude": -55.459392
}
```

### 📌 Obtener la estación más cercana
**GET** `http://127.0.0.1:5000/api/stations/nearest?lat=19.432608&lng=-99.145966`

### 📌 Actualizar una estación
**PUT** `http://127.0.0.1:5000/api/stations/<int:station_id>`

#### 🔹 JSON de ejemplo:
```json
{
  "name": "Moreno",
  "latitude": -57.63,
  "longitude": 36.463
}
```

### 📌 Eliminar una estación
**DELETE** `http://127.0.0.1:5000/api/stations/<int:station_id>`

## 📌 Documentación extra en Notion

Si quieres más detalles sobre este desafío, consulta el siguiente enlace en Notion:
[Desafío Backend Flask](https://candy-cicada-fec.notion.site/Desaf-o-backend-Flask-19f4349a5252808faa32ceb1b8efd617)

---
¡Gracias por visitar este proyecto! 🚀

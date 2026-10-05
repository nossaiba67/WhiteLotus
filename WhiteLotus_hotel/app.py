from flask import Flask
from config import Config
from routes.chambres import chambres_bp
from routes.reservations import reservations_bp

app = Flask(__name__)

# Chargement de la configuration depuis config.py
app.config.from_object(Config)

# Enregistrement des Blueprints (routes)
app.register_blueprint(chambres_bp)
app.register_blueprint(reservations_bp)

if __name__ == '__main__':
    app.run()
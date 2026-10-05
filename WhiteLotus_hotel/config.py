import os

class Config:
    # Clé de sécurité pour les formulaires et sessions Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'white_lotus_secret_key_2026'
    
    # Base de données SQLite
    DATABASE = 'database.db'
    
    # Mode débogage pour le développement
    DEBUG = True
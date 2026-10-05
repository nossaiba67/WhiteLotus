from flask import Blueprint, render_template
import sqlite3

chambres_bp = Blueprint('chambres', __name__)

@chambres_bp.route('/')
def accueil():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Chambres')
    chambres = cursor.fetchall()
    conn.close()
    return render_template('accueil.html', chambres=chambres)
from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

reservations_bp = Blueprint('reservations', __name__)

@reservations_bp.route('/reservation', methods=['GET', 'POST'])
def effectuer_reservation():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        id_chambre = request.form['id_chambre']
        date_arrivee = request.form['date_arrivee']
        date_depart = request.form['date_depart']

        # Vérification : le nom ne doit pas être vide et le départ doit venir après l'arrivée
        if nom.strip() == "" or email.strip() == "" or date_depart <= date_arrivee:
            return "Erreur : données invalides. Vérifiez le nom, l'email et les dates."
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Insérer ou récupérer le client
        cursor.execute('INSERT OR IGNORE INTO Clients (nom, email) VALUES (?, ?)', (nom, email))
        cursor.execute('SELECT id_client FROM Clients WHERE email = ?', (email,))
        id_client = cursor.fetchone()[0]

        # Enregistrer la réservation
        cursor.execute('''
            INSERT INTO Reservations (id_chambre, id_client, date_arrivee, date_depart)
            VALUES (?, ?, ?, ?)
        ''', (id_chambre, id_client, date_arrivee, date_depart))

        conn.commit()
        conn.close()
        return "Réservation enregistrée avec succès !"

    return render_template('reservation.html')
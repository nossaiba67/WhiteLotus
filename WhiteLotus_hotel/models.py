import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Supprimer la table si elle existe pour mettre à jour la structure
    cursor.execute('DROP TABLE IF EXISTS Chambres')

    # Table Chambres
    cursor.execute('''
    CREATE TABLE Chambres (
        id_chambre INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        categorie TEXT,
        prix REAL NOT NULL,
        statut TEXT DEFAULT 'disponible',
        image_url TEXT
    )
    ''')

    # Table Clients
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        id_client INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telephone TEXT
    )
    ''')

    # Table Reservations
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reservations (
        id_reservation INTEGER PRIMARY KEY AUTOINCREMENT,
        id_chambre INTEGER NOT NULL,
        id_client INTEGER NOT NULL,
        date_arrivee DATE NOT NULL,
        date_depart DATE NOT NULL,
        FOREIGN KEY (id_chambre) REFERENCES Chambres(id_chambre),
        FOREIGN KEY (id_client) REFERENCES Clients(id_client)
    )
    ''')

    # Données de test (Chambres avec images différentes)
    cursor.execute('''
        INSERT INTO Chambres (nom, categorie, prix, image_url) 
        VALUES ('Chambre Deluxe 101', 'Suite', 1200, 'https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=800&q=80')
    ''')
    
    cursor.execute('''
        INSERT INTO Chambres (nom, categorie, prix, image_url) 
        VALUES ('Chambre Standard 102', 'Standard', 600, 'https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=800&q=80')
    ''')

    cursor.execute('''
        INSERT INTO Chambres (nom, categorie, prix, image_url) 
        VALUES ('Suite Vue Mer 103', 'Luxe', 1800, 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=800&q=80')
    ''')

    conn.commit()
    conn.close()
    print("Base de données réinitialisée avec succès !")

if __name__ == '__main__':
    init_db()
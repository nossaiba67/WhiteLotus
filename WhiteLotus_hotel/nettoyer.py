import sqlite3

con = sqlite3.connect("database.db")
con.execute("UPDATE Clients SET nom = 'Client Test', email = 'client.test@exemple.com'")
con.commit()
print(con.execute("SELECT * FROM Clients").fetchall())
con.close()
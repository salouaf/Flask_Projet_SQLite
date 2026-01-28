import sqlite3
# Connexion à la base
connection = sqlite3.connect('database.db')

# Exécuter le script SQL initial (clients)
with open('schema.sql') as f:
    connection.executescript(f.read())
    
cur = connection.cursor()

#clients
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

# ----- Books -----
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("Le Petit Prince", "Antoine de Saint-Exupéry", 5))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("1984", "George Orwell", 3))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("Harry Potter à l'école des sorciers", "J.K. Rowling", 7))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("Le Seigneur des Anneaux", "J.R.R. Tolkien", 4))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("Le Comte de Monte-Cristo", "Alexandre Dumas", 6))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("Les Misérables", "Victor Hugo", 2))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("L'Alchimiste", "Paulo Coelho", 5))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("Le Rouge et le Noir", "Stendhal", 3))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("Candide", "Voltaire", 4))
cur.execute("INSERT INTO books (titre, auteur, stock) VALUES (?, ?, ?)",
            ("Les Fleurs du mal", "Charles Baudelaire", 2))

# ----- Loans -----
cur.execute("INSERT INTO loans (nom_client, titre_livre, date_emprunt, date_retour) VALUES (?, ?, ?, ?)",
            ("DUPONT", "1984", "2026-01-28", "2026-02-05"))
cur.execute("INSERT INTO loans (nom_client, titre_livre, date_emprunt, date_retour) VALUES (?, ?, ?, ?)",
            ("LEROUX", "Le Petit Prince", "2026-01-25", "2026-02-01"))
cur.execute("INSERT INTO loans (nom_client, titre_livre, date_emprunt, date_retour) VALUES (?, ?, ?, ?)",
            ("MARTIN", "Harry Potter à l'école des sorciers", "2026-01-27", "2026-02-03"))

# Sauvegarder et fermer
connection.commit()
connection.close()

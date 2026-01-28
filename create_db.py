import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
#test
#test
cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))


#table livre 
cur.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    stock INTEGER DEFAULT 1
)
''')

# Ajouter 10 livres
livres = [
    ("Le Petit Prince", "Antoine de Saint-Exupéry", 5),
    ("1984", "George Orwell", 3),
    ("Harry Potter à l'école des sorciers", "J.K. Rowling", 7),
    ("Le Seigneur des Anneaux", "J.R.R. Tolkien", 4),
    ("Le Comte de Monte-Cristo", "Alexandre Dumas", 6),
    ("Les Misérables", "Victor Hugo", 2),
    ("L'Alchimiste", "Paulo Coelho", 5),
    ("Le Rouge et le Noir", "Stendhal", 3),
    ("Candide", "Voltaire", 4),
    ("Les Fleurs du mal", "Charles Baudelaire", 2)
]

for livre in livres:
    cur.execute('INSERT OR IGNORE INTO books (titre, auteur, stock) VALUES (?, ?, ?)', livre)

# ----- Table Loans -----
cur.execute('''
CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    user_id INTEGER,
    date_emprunt TEXT,
    date_retour TEXT,
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(user_id) REFERENCES clients(id)
)
''')

connection.commit()
connection.close()

import sqlite3

# Connexion à la base (elle sera créée si elle n'existe pas)
connection = sqlite3.connect('database_tache.db')

# Exécuter le script SQL pour créer la table taches
with open('schema_tache.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insérer des tâches initiales
cur.execute("INSERT INTO taches (nom, description) VALUES (?, ?)", 
            ("Ajouter une tâche", "Formulaire dans une page JSP"))
cur.execute("INSERT INTO taches (nom, description) VALUES (?, ?)", 
            ("Afficher les tâches", "Liste visible avec titre et description"))
cur.execute("INSERT INTO taches (nom, description) VALUES (?, ?)", 
            ("Accueil", "Page d'accueil avec navigation vers les autres fonctionnalités"))
cur.execute("INSERT INTO taches (nom, description) VALUES (?, ?)", 
            ("Suppression d’une tâche", "Permettre la suppression d'une tâche"))

# Valider les changements
connection.commit()
connection.close()

print("Base database_tache.db créée et tâches initiales ajoutées !")

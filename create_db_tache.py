import sqlite3

# Connexion à la base (elle sera créée si elle n'existe pas)
connection = sqlite3.connect('database_tache.db')

# Exécuter le script SQL pour créer la table taches
with open('schema_tache.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insérer des tâches initiales
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Problème de connexion VPN", "L'utilisateur ne peut pas se connecter au VPN depuis son ordinateur"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Erreur application CRM", "L'application CRM plante lors de la création d'un nouveau client"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Imprimante réseau hors service", "Impossible d'imprimer depuis l'ordinateur du bureau 301"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Mise à jour Windows", "Mettre à jour tous les postes avec le dernier patch de sécurité"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Problème email Outlook", "Les emails ne se synchronisent pas correctement pour certains utilisateurs"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Création compte utilisateur", "Ajouter un nouvel utilisateur au domaine avec droits standards"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Problème de mot de passe", "Réinitialiser le mot de passe pour l'utilisateur Dupont"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Installation logiciel", "Installer le logiciel de gestion de projet sur les postes de l'équipe"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Accès base de données", "L'utilisateur X n'a pas les droits pour accéder à la base de données de test"))
cur.execute("INSERT INTO tickets (titre, description) VALUES (?, ?)", ("Audit sécurité", "Vérifier les journaux et les permissions sur les serveurs internes"))


# Valider les changements
connection.commit()
connection.close()

print("Base database_tache.db créée et tâches initiales ajoutées !")

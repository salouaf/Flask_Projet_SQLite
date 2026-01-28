from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

  # Si l'utilisateur est authentifié
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'user' and password == '12345':
            session['authentifie'] = True
            session['role'] = 'user'
            return redirect(url_for('fiche_nom_form'))  # vers le formulaire de recherche
        # ici tu peux garder admin si tu veux
        elif username == 'admin' and password == 'password':
            session['authentifie'] = True
            session['role'] = 'admin'
            return redirect(url_for('lecture'))
        else :
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')  # afficher le formulaire

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']

    # Connexion à la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/')  # Rediriger vers la page d'accueil après l'enregistrement
                                                                                                             
@app.route('/fiche_nom/<string:nom_client>')
def fiche_nom_result(nom_client):
    if not session.get('authentifie') or session.get('role') != 'user':
        return redirect(url_for('authentification'))

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE nom = ?', (nom_client,))
    data = cursor.fetchall()
    conn.close()

    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

#créer la route/fiche_nom pour creer formulaire pour saisir le nom du client
@app.route('/fiche_nom', methods=['GET', 'POST'])
def fiche_nom_form():
    if not session.get('authentifie') or session.get('role') != 'user':
        return redirect(url_for('authentification'))

    if request.method == 'POST':
        nom_client = request.form['nom_client']
        return redirect(url_for('fiche_nom_result', nom_client=nom_client))

    return render_template('formulaire_nom.html')


#bibliotheque
@app.route('/books')
def list_books():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)
if __name__ == "__main__":
  app.run(debug=True)

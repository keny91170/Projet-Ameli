from flask import Flask, render_template, request
import matplotlib
import model.db as db
from model.db import get_resultats_filtrage
 
app = Flask(__name__)
 
@app.route('/')
def accueil():
    # Affichage du template
    return render_template('index.html')
 
# Route pour afficher le contenu de la table "demographie"
@app.route('/afficher_demographie')
def afficher_demographie():

    order_by = request.args.get('order_by', 'id_profession')
    # Obtention des departements
    demographie = db.get_demographie(order_by)
 
    # Affichage du template avec les résultats
    return render_template('afficher_demographie.html', demographie=demographie, order_by=order_by)
 

# Route pour afficher le contenu de la table "demographie"
@app.route('/afficher_prescription')
def afficher_prescription():
    # Obtention du paramètre d'ordre de l'URL
    order_by = request.args.get('order_by', 'id_prescription')

    # Obtention de la liste des étudiants triée
    prescription = db.get_prescription(order_by)

    # Affichage du template avec les résultats
    return render_template('afficher_prescription.html', prescription=prescription, order_by=order_by)

# Route pour afficher le contenu de la table "demographie"
@app.route('/afficher_departement')
def afficher_departement():

    order_by = request.args.get('order_by', 'departement')
    # Obtention des departements
    departement = db.get_departement(order_by)
 
    # Affichage du template avec les résultats
    return render_template('afficher_departement.html', departement=departement, order_by=order_by)

@app.route('/graphique')
def graphique():

    chemin = db.generate_demographie_chart()
    
    return render_template('graphique.html', chemin=chemin,)

@app.route('/afficher_profession')
def afficher_profession():

    order_by = request.args.get('order_by', 'id_profession')
    # Obtention des professions
    profession = db.get_profession(order_by)
 
    # Affichage du template avec les résultats
    return render_template('afficher_profession.html', profession=profession, order_by=order_by)

"""@app.route('/afficher_honoraires')
def afficher_honoraires():

    order_by = request.args.get('order_by', 'id_honoraires')
    # Obtention des departements
    honoraires = db.get_honoraires(order_by)
 
    # Affichage du template avec les résultats
    return render_template('afficher_honoraires.html', honoraires=honoraires, order_by=order_by)"""

@app.route('/afficher_region')
def afficher_region():

    order_by = request.args.get('order_by', 'region')
    # Obtention des departements
    region = db.get_region(order_by)
 
    # Affichage du template avec les résultats
    return render_template('afficher_region.html', region=region, order_by=order_by)


@app.route('/contenu_table') 
def contenu_table():
    # Affichage du template
    return render_template('contenu_table.html')

#DEBUT PAGE RECHERCHE DONNES

@app.route('/recherche_donnees') 
def recherche_donnees():
    # Récupérer les données de la base
    fprofession, fannee, fdepartement = db.get_formulaire()

    # Passer les listes au template
    return render_template('recherche_donnees.html', 
                           fprofession=fprofession, 
                           fannee=fannee, 
                           fdepartement=fdepartement)

@app.route('/resultats') 
def resultats():
    # Récupérer les paramètres de recherche
    profession = request.args.get('profession', 'Toutes les professions')
    departement = request.args.get('departement', 'tous les départements')
    annee = request.args.get('annee', 'toutes les années')

    # Obtenir les résultats filtrés
    resultats = db.get_resultats_filtrage(profession, departement, annee)

    # Créer un titre dynamique pour le tableau
    titre = f"{profession} en {annee} dans {departement}"

    # Passer les résultats et le titre au template
    return render_template('resultats.html', 
                           resultats=resultats.to_dict(orient='records'), 
                           titre=titre)

#FIN PAGE RECHERCHE DONNEES

@app.route('/afficher_honoraires')
def afficher_honoraires():

    order_by = request.args.get('order_by', 'annee')
    honoraire = db.get_honoraires_annee(order_by)

    return render_template('afficher_honoraires.html', honoraire=honoraire, order_by=order_by)



@app.route('/choix_des_tables')
def choix_des_tables():
    # Code pour gérer le choix des tables
    return render_template('choix_des_tables.html')

if __name__ == '__main__':
    app.run(debug=True)
 


import matplotlib.pyplot as plt
import model.db as db
from io import BytesIO
import base64

# Fonction pour générer l'histogramme des notes et le convertir en image
def generate_histogram():
    # Récupération des notes des étudiants
    marks = db.get_marks()

    # Génération de l'histogramme avec Matplotlib
    intervalles = list(range(0, 105, 5))
    plt.hist(marks, bins=intervalles, edgecolor='black')
    plt.xlabel('Notes')
    plt.ylabel('Nombre d\'étudiants')
    plt.title('Répartition des notes des étudiants')
    plt.grid(axis='y', alpha=0.75)

    # Convertion de l'histogramme en image
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Convertion de l'image en format base64 pour l'inclure dans le template
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')
    return f'data:image/png;base64,{image_base64}'

# Fonction pour générer les boites à moustache des notes et le convertir en image
def generate_boxplot(df):
    # Générer un graphique à boîtes à moustaches avec Matplotlib
    plt.figure(figsize=(8, 6))
    boxplot = df.boxplot(column='mark', by='class', vert=False)
    plt.title('')  # Supprimer le titre par défaut
    plt.suptitle('Boîtes à moustaches par classe')
    plt.xlabel('Note')
    plt.ylabel('Classe')
    # Ajuster les marges pour éviter la coupure de la légende des axes Y
    plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.2)

    # Convertion de l'histogramme en image
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Convertion de l'image en format base64 pour l'inclure dans le template
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    return f'data:image/png;base64,{image_base64}'
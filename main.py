from utils.filter_columns import filter_csv_columns
from utils.clean_data import get_clean_work_time
from utils.filter_rows import filter_rows
import matplotlib.pyplot as plt

# Chemins vers les fichiers
work_time_file = "data/temps-de-travail-annuel-depuis-1851.csv"
frequentation_file = "data/frequentation-gares.csv"

# Colonnes d'intérêt
work_time_columns = [
    "Date",
    "Temps annuel de travail (SNCF)",
    "Temps annuel de travail (France)"
]

frequentation_columns = [
    "Nom de la gare",
    "Code postal",
    "Total Voyageurs + Non voyageurs 2017",
    "Total Voyageurs + Non voyageurs 2018"
]

# Filtrage des colonnes
work_time = filter_csv_columns(work_time_file, work_time_columns, sep=';')
frequentation = filter_csv_columns(frequentation_file, frequentation_columns, sep=';')

# Filtrage des lignes pour work_time (2016 et 2018)
work_time_filtered = filter_rows(
    work_time, 
    column_conditions={"Date": [2016,2017,2018]}
)

# Filtrage des lignes pour frequentation (Code postal commençant par 7, max 3 lignes)
frequentation_filtered = filter_rows(
    frequentation, 
    startswith_conditions={"Code postal": "83"},
    limit=8, 
)

print("Work Time Filtré :")
print(work_time_filtered)

print("\nFrequentation Filtrée :")
print(frequentation_filtered)


def get_frequentation_diagram(frequentation_df):
    # Vérification des colonnes requises
    required_columns = [
        'Nom de la gare', 
        'Total Voyageurs + Non voyageurs 2017', 
        'Total Voyageurs + Non voyageurs 2018'
    ]
    for col in required_columns:
        if col not in frequentation_df.columns:
            raise ValueError(f"Colonne manquante dans le DataFrame : {col}")
    
    # Configuration des données
    frequentation_df = frequentation_df.set_index('Nom de la gare')[
        ['Total Voyageurs + Non voyageurs 2017', 'Total Voyageurs + Non voyageurs 2018']
    ]
    
    # Création du graphique
    frequentation_df.plot(kind='bar', figsize=(12, 6))
    plt.title("Comparaison fréquentation des gares entre 2017 et 2018")
    plt.xlabel("Nom de la gare")
    plt.ylabel("Total voyageurs")
    plt.xticks(rotation=45)  # Rotation des noms de gare
    plt.grid(axis='y')       # Grille sur l'axe Y
    plt.legend(title="Année")  # Légende avec titre
    plt.tight_layout()  # Ajuste la mise en page pour éviter le chevauchement
    plt.show()

# Exemple d'utilisation
get_frequentation_diagram(frequentation_filtered)
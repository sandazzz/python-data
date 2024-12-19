from utils.filter_columns import filter_csv_columns
from utils.clean_data import get_clean_work_time
from utils.filter_rows import filter_rows

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

# Application de la fonction
work_time = filter_csv_columns(work_time_file, work_time_columns, sep=';')
frequentation = filter_csv_columns(frequentation_file, frequentation_columns, sep=';')

# Nettoyage des données pour work_time
work_time_clean = get_clean_work_time(work_time_file)

print("Work Time DataFrame :")
print(work_time_clean)

print("\nFrequentation DataFrame :")
print(frequentation)


# Filtrage des lignes pour work_time (2017 et 2018)
work_time_filtered = filter_rows(work_time, column_conditions={"Date": [2017, 2018]})

# Filtrage des lignes pour frequentation (Code postal commençant par 7, max 3 lignes)
frequentation_filtered = filter_rows(
    frequentation, 
    startswith_conditions={"Code postal": "7"}, 
    limit=3
)

print("Work Time Filtré :")
print(work_time_filtered)

print("\nFrequentation Filtrée :")
print(frequentation_filtered)
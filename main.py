from utils.filter_columns import filter_csv_columns
from utils.clean_data import get_clean_work_time
from utils.filter_rows import filter_rows
from chart.plot_time_series import plot_time_series
from chart.frequentation_diagram import get_frequentation_diagram

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


# Exemple d'utilisation
get_frequentation_diagram(frequentation_filtered)


# # Filtrage des années 2017 et 2018 pour la démonstration
# work_time_filtered = work_time[work_time['Date'].isin([2017, 2018])]

# # Colonnes pour l'axe Y
# y_columns = [
#     "Temps annuel de travail (SNCF)", 
#     "Temps annuel de travail (France)"
# ]

# # Affichage du graphique

# plot_time_series(
#     work_time_filtered, 
#     x_col="Date", 
#     y_cols=y_columns, 
#     title="Évolution du Temps Annuel de Travail (2017-2018)",
#     xlabel="Année",
#     ylabel="Temps annuel de travail (heures)"
# )

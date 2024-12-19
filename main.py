import pandas as pd
from utils.extract_columns import get_interesting_columns
from utils.clean_data import get_clean_work_time

work_time_file = get_clean_work_time('data/temps-de-travail-annuel-depuis-1851.csv')
work_time_columns = [
    "Date",
    "Temps annuel de travail (SNCF)",
    "Temps annuel de travail (France)"
]

work_time = get_interesting_columns(work_time_file, work_time_columns)

frequentation_file = pd.read_csv("data/frequentation-gares.csv", sep=';')
frequentation_columns = [
    "Nom de la gare",
    "Code postal",
    "Total Voyageurs + Non voyageurs 2017",
    "Total Voyageurs + Non voyageurs 2018"
]
frequentation = get_interesting_columns(frequentation_file, frequentation_columns)

print(work_time)
print(frequentation)
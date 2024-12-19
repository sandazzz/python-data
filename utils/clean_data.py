#clean_data.py
import pandas as pd

def get_clean_work_time(work_time_path):
    return (
        pd.read_csv(work_time_path, sep=';', encoding='utf-8')
        .drop_duplicates()
        .fillna({'Temps annuel de travail (SNCF)': 0,
                 'Temps annuel de travail (France)': 0,
                 'Commentaires': ''})
        .astype({'Date': int,
                 'Temps annuel de travail (SNCF)': int,
                 'Temps annuel de travail (France)': int})
        .assign(Commentaires=lambda x: x['Commentaires'].str.strip())
    )

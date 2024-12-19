import matplotlib.pyplot as plt

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

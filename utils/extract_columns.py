#extract_columns.py
import pandas as pd

def get_interesting_columns(df, columns): 
    missing_colomns = [col for col in columns if col not in df.columns]
    if missing_colomns:
        print(f"colomn missing")
        return pd.DataFrame()
    return df[columns]

#filter_row.py

def filter_rows(df, column_conditions=None, startswith_conditions=None, limit=None):
    if column_conditions:
        for col, values in column_conditions.items():
            df = df[df[col].isin(values)]
    
    if startswith_conditions:
        for col, prefix in startswith_conditions.items():
            df = df[df[col].astype(str).str.startswith(prefix)]
    
    if limit:
        df = df.head(limit)
    
    return df

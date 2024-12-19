import matplotlib.pyplot as plt

def plot_time_series(df, x_col, y_cols, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    
    for y_col in y_cols:
        plt.plot(df[x_col], df[y_col], label=y_col, marker='o')
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

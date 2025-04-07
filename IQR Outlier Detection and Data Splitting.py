import sys
import pandas as pd

def calculate_statistics(data):
    stats = {
        'min': data.min(),
        'max': data.max(),
        'mean': data.mean(),
        'median': data.median(),
        'std': data.std(),
        'iqr': data.quantile(0.75) - data.quantile(0.25)  
    }
    return stats

def print_statistics(name, stats):
    print(f"\n{name} Statistics:")
    for stat, value in stats.items():
        print(f"{stat.capitalize()}: {value}")
            
def main():
    if len(sys.argv) not in [3, 4]:
        print("Usage: python script.py <filename> <column_index> [-h]")
        sys.exit(1)

    filename = sys.argv[1]
    column_index = int(sys.argv[2])
    has_header = len(sys.argv) == 4 and sys.argv[3] == '-h'

    try:
        if has_header:
            data = pd.read_csv(filename)
        else:
            data = pd.read_csv(filename, header=None)
            data.columns = [f"Column {i}" for i in range(data.shape[1])]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: File '{filename}' is empty.")
        sys.exit(1)

    if column_index >= len(data.columns):
        print(f"Error: Invalid column index {column_index}. Dataset has only {len(data.columns)} columns.")
        sys.exit(1)

    data_column = data.iloc[:, column_index]
    print(f"Column {column_index} successfully loaded:")
    print(data_column)

    
    Q1 = data_column.quantile(0.25)
    Q3 = data_column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = pd.concat([data[data_column < lower_bound], data[data_column > upper_bound]])
    non_outliers = data[(data_column >= lower_bound) & (data_column <= upper_bound)]
    original_stats = calculate_statistics(data_column)
    outliers_stats = calculate_statistics(outliers.iloc[:, column_index]) if not outliers.empty else {}
    non_outliers_stats = calculate_statistics(non_outliers.iloc[:, column_index])
    print_statistics("Original Dataset", original_stats)
    if outliers.empty:
        print("\nNo outliers detected.")
    else:
        print_statistics("Outliers", outliers_stats)
    print_statistics("Non-Outliers", non_outliers_stats)
    base_filename = filename.rsplit('.', 1)[0]
    outliers.to_csv(f"{base_filename}_outliers.csv", index=False)
    non_outliers.to_csv(f"{base_filename}_nonoutliers.csv", index=False)
    print(f"\nDatasets saved: {base_filename}_outliers.csv and {base_filename}_nonoutliers.csv")
if __name__ == "__main__":
    main()
# 📊 Outlier Detection and Data Splitting using IQR

## 📌 Project Objective

This Python script:
- Accepts a CSV file and a target column as input
- Performs **Interquartile Range (IQR)** based outlier detection
- Splits the dataset into two parts: **outliers** and **non-outliers**
- Calculates and **prints summary statistics** (mean, median, std, IQR) to the console
- Saves both subsets as **separate CSV files** (`outliers.csv`, `non_outliers.csv`)

> ⚠️ Note: No plotting or HTML reports are included. The output is purely statistical and text-based.

---

## 🧠 Skills Demonstrated

- CLI-based data preprocessing and outlier detection
- Efficient reading, writing, and filtering of CSV data using Python
- Statistical analysis using the IQR method
- File I/O operations with pandas
- Modular code design with argument handling and clean output

---

## 🧰 Libraries Used

- `pandas`: for data manipulation and analysis  
- `numpy`: for numerical computations  
- `sys`: to handle command-line arguments  

---

## 🚀 How It Works

### 📁 Steps Performed

1. **Import Required Libraries**
2. **Accept Command-Line Arguments**  
   `python outlier_split.py <input_file.csv> <column_index>`
3. **Read the Input CSV**
4. **Extract the Target Column**
5. **Perform IQR-Based Outlier Detection**
6. **Calculate and Print Summary Statistics**  
   (Mean, Median, Std Dev, IQR, Min, Max)
7. **Save Subsets as CSV Files**  
   - `outliers.csv`  
   - `non_outliers.csv`

---

## ⚙️ Usage & Example Output

```bash
python outlier_split.py data.csv 2

```

```bash
Example Output:

Original Data Summary:
Mean: 57.2 | Median: 55.0 | Std Dev: 12.6 | IQR: 15.5

Outlier Subset Summary:
Mean: 98.3 | Count: 6

Non-Outlier Subset Summary:
Mean: 53.1 | Count: 94
```


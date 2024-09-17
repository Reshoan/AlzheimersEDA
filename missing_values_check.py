import pandas as pd

# Loading the dataset
df = pd.read_csv('alzheimers_disease_data.csv')

# Checking for missing values
missing_values = df.isnull().sum()
print("Missing Values in Each Column:\n", missing_values)

# Checking the percentage of missing values
missing_percentage = (df.isnull().sum() / len(df)) * 100
print("Percentage of Missing Values in Each Column:\n", missing_percentage)

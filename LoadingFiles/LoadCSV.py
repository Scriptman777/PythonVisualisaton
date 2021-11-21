import csv
import pandas as pd

# Reading CSV with Python
with open('KIKM_PGRF2.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    lines = []

    for row in reader:
        # Work with read data
        lines.append(row)

print("Lines:")
print(lines)


# Reading CSV with pandas

df = pd.read_csv('KIKM_PGRF2.csv', sep=';')

print("DataFrame:")
print(df)
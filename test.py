import pandas as pd
import requests

# Google Sheets file ID
file_id = '1wo5BtRrOsgX--2ZO-hwOJLoPGKrAYDyH'

# URL to download the file in Excel format
url = f'https://docs.google.com/spreadsheets/d/{file_id}/export?format=xlsx'

# Output file name
output = 'Suivi_Analyse_Mobile_préparaé.xlsx'

# Download the file
response = requests.get(url)
with open(output, 'wb') as file:
    file.write(response.content)

# Load the Excel file into a DataFrame
df = pd.read_excel(output, sheet_name="QT_intake")
print(df.head())

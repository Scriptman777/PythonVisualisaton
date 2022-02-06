from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


# Load table from http://www.pla.cz/portal/sap/cz/PC/Mereni.aspx?id=56&oid=1

# Open url
page_url = urlopen("http://www.pla.cz/portal/sap/cz/PC/Mereni.aspx?id=56&oid=1")
# Read whole page
all_content = page_url.read().decode("utf-8")
# Create a BeautifulSoup object
soup = BeautifulSoup(all_content, "html.parser")
# There is only one ID on a page
table = soup.find(id='ObsahCPH_DataMereniGV')
# Create DataFrame from table
df = pd.read_html(str(table))[0]
# Rename unnamed date column
df = df.rename(columns={'Unnamed: 0': 'Date'})
# Change datatype to datetime
df['Date'] = pd.to_datetime(df['Date'])

print(df)
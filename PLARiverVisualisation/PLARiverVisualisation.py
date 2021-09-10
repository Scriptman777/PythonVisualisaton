from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import plotly.express as px


webpage = urlopen("http://www.pla.cz/portal/sap/cz/PC/Prehled.aspx")
page_content = webpage.read().decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")

river_links = soup.find_all('a', class_="odkazNaStaniciVPrehledu")
river_urls = []

for link in river_links:
    river_urls.append('http://www.pla.cz/portal/sap/cz/PC/' + link.get('href'))

#for url in river_urls:
url = river_urls[0]
subpage = urlopen(url)
page_content = subpage.read().decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")
table = soup.find(id='ObsahCPH_DataMereniGV')
df = pd.read_html(str(table))[0]

fig = px.area(df, x='Unnamed: 0', y='H [cm]')

fig.write_html("Plotly output.html")
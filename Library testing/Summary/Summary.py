import pandas
import plotly.express as px

df = pandas.read_csv("Summary.csv")

fig = px.bar(df, x="Knihovna", y=["Vstupní formáty", "Výstupní formáty", "Typy grafů", "Možnosti přizpůsobení", "Možnosti interaktivity"], title="Shrnutí", labels={'value': 'Body'}, color_discrete_sequence=px.colors.qualitative.G10)
fig.update_layout(legend_title="Kategorie hodnocení")

fig.write_image("Summary.svg")
fig.write_image("Summary.png")
fig.show()

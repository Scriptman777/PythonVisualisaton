import mysql.connector
import numpy as np
from collections import Counter
import pygal
import webbrowser
from pygal.style import Style, CleanStyle

def create_labels(edges):
    labels = []
    labels.append('Less than ' + str(edges[0]))
    for x in range(0,len(edges)-1):
        labels.append(str('%.1f' % edges[x]) + ' - ' + str('%.1f' % edges[x+1]))
    return labels


def read_db(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def untuple(tuple_list):
    list = []
    for value in tuple_list:
        list.append(value[0])
    return list


connection = mysql.connector.connect(host="localhost",user="root",passwd="password",database="Marketing")

query = "SELECT age FROM MARKETING_DATA where gender = 'F';"
result = read_db(query)
female_ages = untuple(result)

query = "SELECT age FROM MARKETING_DATA where gender = 'M';"
result = read_db(query)
male_ages = untuple(result)

query = "SELECT size FROM MARKETING_DATA;"
result = read_db(query)
size_result = Counter(untuple(result))
size_result = size_result.most_common()


# Visualize

female_ages_chart = pygal.Bar()
female_ages_chart.title = 'Female ages'
female_ages_chart.add('Female ages', female_ages_hist)
female_ages_chart.x_labels = create_labels(edges_f)
female_ages_chart.render_to_file('fig1.svg')

style = Style(colors=('#0022FF', '#000000'))
male_ages_chart = pygal.Histogram(style=style)
male_ages_chart.title = 'Male ages'
datalist = []
datalist.append((male_ages_hist[0],0,edges_m[0]))
for x in range(1,len(male_ages_hist)):
    datalist.append((male_ages_hist[x],edges_m[x-1],edges_m[x]))
male_ages_chart.add('Male ages', datalist)
male_ages_chart.render_to_file('fig2.svg')

ratio_chart = pygal.Pie()
ratio_chart.title = 'Female to male ratio'
ratio_chart.add('Female',len(female_ages))
ratio_chart.add('Male',len(male_ages))
ratio_chart.render_to_file('fig3.svg')

size_chart = pygal.HorizontalBar(style=CleanStyle)
size_chart.title = 'Most common sizes'
for size_data in size_result:
    size_chart.add(size_data[0],size_data[1])
size_chart.render_to_file('fig4.svg')


#Build HTML

html = open('Pygal_output.html','w')
html.write("""
<html>
<head>
<title>Marketing data visualisation</title>
<style>
  object {width:40%; height:auto;}
</style>
</head><body>""" + '\n')
html.write("""<object type='image/svg+xml' data='fig1.svg'></object>""")
html.write("""<object type='image/svg+xml' data='fig2.svg'></object>""" + '\n')
html.write("""<object type='image/svg+xml' data='fig3.svg'></object>""")
html.write("""<object type='image/svg+xml' data='fig4.svg'></object>""" + '\n')
html.write('</body></html>')  
html.close()

webbrowser.open('Pygal_output.html')
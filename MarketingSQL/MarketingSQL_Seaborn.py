import mysql.connector

import numpy as np
from collections import Counter

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

def recolor_hist(N, bins, patches, cmap):
    fracs = N / N.max()
    norm = colors.Normalize(fracs.min(), fracs.max())
    map = plt.cm.get_cmap(cmap)
    for thisfrac, thispatch in zip(fracs, patches):
        color = map(norm(thisfrac))
        thispatch.set_facecolor(color)


connection = mysql.connector.connect(host="localhost",user="root",passwd="password",database="Marketing")


query = "SELECT age FROM MARKETING_DATA where gender = 'M';"
result = read_db(query)
male_ages = untuple(result)

query = "SELECT age FROM MARKETING_DATA where gender = 'F';"
result = read_db(query)
female_ages = untuple(result)

query = "SELECT size FROM MARKETING_DATA;"
result = read_db(query)
size_result = Counter(untuple(result))
size_result = size_result.most_common()
size_result = list(zip(*size_result))
sizes = list(size_result[0])
size_counts = list(size_result[1])

#TODO, visualize

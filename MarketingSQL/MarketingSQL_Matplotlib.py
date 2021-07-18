import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.colors as colors
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
sizes = list(size_result.keys())
size_counts = list(size_result.values())

fig, axs = plt.subplots(2, 3)
N, bins, patches = axs[0][0].hist(female_ages, bins=10)
axs[0][0].set_title("Female ages")
recolor_hist(N, bins, patches, "spring")

N, bins, patches = axs[0][1].hist(male_ages, bins=10)
axs[0][1].set_title("Male ages")
recolor_hist(N, bins, patches, "winter")

axs[0][2].pie([len(female_ages),len(male_ages)],labels=["F","M"])


axs[1][0].barh(sizes, size_counts)



plt.show()
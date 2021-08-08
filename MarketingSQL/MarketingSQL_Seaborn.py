import mysql.connector
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


connection = mysql.connector.connect(host="localhost",user="root",passwd="password",database="Marketing")

query = "SELECT age, has_card FROM MARKETING_DATA where gender = 'F';"
result_female = read_db(query)
female_ages = untuple(result_female)

query = "SELECT age, has_card FROM MARKETING_DATA where gender = 'M';"
result_male = read_db(query)
male_ages = untuple(result_male)

query = "SELECT size FROM MARKETING_DATA;"
result = read_db(query)
size_result = Counter(untuple(result))
size_result = size_result.most_common()
size_result = list(zip(*size_result))
sizes = list(size_result[0])
size_counts = list(size_result[1])

sns.set()
sns.set_theme(style="darkgrid")

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

sns.histplot(ax=axs[0][0], data=female_ages, color="red")
axs[0][0].set_title("Female ages")

sns.histplot(ax=axs[0][1], data=male_ages, color="blue")
axs[0][1].set_title("Male ages")


separate = list(zip(*result_male))
separate2 = list(zip(*result_female))

data = {"age": list(separate[0]), "card": list(separate[1]), "gender": np.repeat('Male',len(separate[0])).tolist()}

data["age"].extend(list(separate2[0]))
data["card"].extend(list(separate2[1]))
data["card"] = ["Yes" if x=='1' else "No" for x in data["card"]]
data["gender"].extend(np.repeat('Female',len(separate2[0])).tolist())
data_frame = pd.DataFrame(data=data)
sns.violinplot(ax=axs[1][0], data=data_frame, x="gender", y="age", hue="card", split=True, palette=['r','g'])
axs[1][0].set_title("Age distribution by gender and card ownership")

size_data = {"sizes": sizes, "count": size_counts}
sns.barplot(ax=axs[1][1], y="sizes", x="count", data=size_data, palette="rocket")
axs[1][1].set_title("Most common sizes")

plt.show()

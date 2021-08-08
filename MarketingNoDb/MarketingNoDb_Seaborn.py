import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def untuple(tuple_list):
    list = []
    for value in tuple_list:
        list.append(value[0])
    return list


result_female = [(44, '1'), (36, '1'), (40, '0'), (40, '1'), (44, '0'), (47, '1'), (28, '1'), (44, '1'), (43, '1'), (43, '1'), (49, '1'), (50, '0'), (48, '1'), (32, '1'), (38, '1'), (51, '0'), (27, '0'), (28, '1'), (35, '1'), (40, '0'), (38, '0'), (51, '0'), (36, '1'), (37, '1'), (37, '0'), (48, '0'), (43, '0'), (56, '0'), (31, '0'), (39, '1'), (34, '0'), (42, '0'), (45, '0'), (41, '0'), (36, '1'), (35, '1'), (34, '1'), (53, '0'), (50, '0'), (36, '1'), (31, '1'), (41, '1'), (45, '0'), (37, '1'), (48, '1'), (34, '1'), (26, '1'), (32, '1'), (38, '1'), (57, '1'), (52, '1'), (39, '1'), (39, '0'), (33, '0'), (44, '0'), (38, '1'), (37, '0'), (33, '0'), (31, '0'), (26, '0'), (45, '0'), (27, '1'), (37, '0'), (26, '1'), (39, '0'), (46, '1'), (24, '1'), (31, '1'), (50, '0'), (49, '1'), (39, '0'), (41, '0'), (39, '0'), (35, '1'), (43, '1'), (45, '1'), (45, '0'), (42, '0'), (41, '1'), (36, '0'), (36, '0'), (44, '1'), (31, '0'), (47, '1'), (49, '1'), (26, '0'), (55, '0'), (51, '1'), (48, '0'), (35, '0'), (38, '0'), (26, '0'), (51, '1'), (53, '1'), (34, '0'), (41, '1'), (52, '1'), (43, '1'), (27, '1'), (33, '1'), (40, '0'), (39, '1'), (28, '0'), (29, '0'), (35, '1'), (45, '1'), (35, '1'), (46, '0'), (42, '0'), (36, '1'), (38, '1'), (31, '1'), (48, '0'), (40, '0'), (47, '1'), (41, '0'), (43, '0'), (31, '1'), (31, '0'), (47, '0'), (32, '1'), (50, '0'), (46, '1'), (46, '0'), (29, '1'), (49, '1'), (41, '1'), (35, '1'), (32, '0'), (44, '0'), (38, '0'), (39, '1'), (52, '0'), (38, '0'), (37, '0'), (39, '0'), (36, '0'), (29, '1'), (40, '0'), (38, '1'), (24, '0'), (51, '0'), (56, '1'), (33, '0'), (48, '1'), (39, '0'), (54, '0'), (54, '0'), (43, '1'), (42, '1'), (41, '0'), (54, '0'), (47, '1'), (39, '1'), (60, '0'), (26, '0'), (44, '0'), (47, '0'), (29, '0'), (37, '0'), (36, '0'), (50, '0'), (36, '0'), (37, '0'), (42, '0'), (24, '0'), (39, '1'), (37, '0'), (49, '0'), (30, '0'), (38, '0'), (58, '1'), (41, '1'), (29, '1'), (40, '1'), (39, '1'), (47, '1'), (39, '1'), (45, '1'), (35, '1'), (42, '1'), (47, '0'), (31, '1'), (41, '1'), (38, '0'), (39, '0'), (33, '1'), (39, '0'), (40, '1'), (44, '0'), (34, '0'), (37, '0'), (41, '0'), (53, '0'), (27, '0'), (42, '1'), (36, '0'), (53, '1'), (36, '1'), (31, '1'), (33, '0'), (42, '1'), (45, '0'), (52, '0'), (38, '1'), (41, '1'), (45, '0'), (37, '1'), (52, '1'), (37, '0'), (40, '1'), (35, '0'), (45, '0'), (44, '1'), (28, '1'), (46, '1'), (45, '1'), (41, '0'), (44, '1'), (46, '0'), (39, '1'), (54, '0'), (40, '0'), (44, '0'), (41, '0'), (47, '1'), (44, '0'), (41, '1'), (40, '0'), (44, '0'), (53, '0'), (47, '0'), (46, '1'), (47, '1'), (33, '1'), (50, '1'), (37, '1'), (41, '1'), (40, '1'), (29, '0'), (41, '0'), (46, '1'), (42, '1'), (48, '1'), (49, '1'), (21, '0'), (38, '1'), (54, '1'), (46, '0'), (25, '1'), (39, '1'), (28, '0'), (29, '1'), (43, '1'), (52, '1'), (43, '0'), (29, '0'), (46, '0'), (39, '1'), (32, '1'), (48, '1'), (41, '0'), (46, '0'), (30, '0'), (43, '0'), (34, '1'), (36, '1'), (40, '1'), (51, '1'), (38, '1'), (53, '1'), (45, '1'), (41, '1'), (32, '0'), (47, '1'), (42, '1'), (45, '1'), (46, '1'), (40, '1'), (47, '0'), (50, '0'), (37, '0'), (25, '0'), (39, '1'), (39, '1'), (48, '0'), (41, '0'), (43, '0'), (30, '1'), (24, '1'), (34, '0'), (29, '0'), (39, '0'), (44, '0'), (48, '1'), (31, '1'), (47, '1'), (44, '1'), (33, '0'), (31, '0'), (34, '1'), (57, '1'), (55, '1'), (32, '1'), (44, '0'), (51, '1'), (45, '1'), (40, '1'), (43, '0'), (45, '0'), (34, '1'), (40, '0'), (28, '0'), (33, '0'), (43, '1'), (33, '0'), (34, '0'), (30, '1'), (45, '0'), (39, '1'), (37, '1'), (44, '1'), (30, '0'), (51, '0'), (33, '0'), (45, '1'), (47, '0'), (43, '1'), (25, '1'), (34, '0'), (31, '1'), (42, '1'), (33, '1'), (51, '1'), (41, '1'), (35, '1'), (44, '0'), (34, '1'), (38, '0'), (49, '1'), (55, '0'), (32, '1'), (46, '1'), (50, '1'), (41, '1'), (33, '0'), (32, '1'), (48, '0'), (37, '1'), (41, '0'), (24, '0'), (57, '1'), (49, '1'), (38, '0'), (51, '0'), (42, '0'), (46, '1'), (29, '0'), (24, '1'), (37, '1'), (39, '0'), (50, '0'), (26, '0'), (44, '1'), (39, '1'), (51, '1'), (47, '0'), (29, '1'), (44, '1'), (45, '1'), (43, '0'), (41, '1'), (30, '1'), (40, '1'), (35, '1'), (45, '0'), (55, '1'), (45, '0'), (35, '1'), (36, '0'), (37, '1'), (44, '0'), (53, '1'), (45, '1'), (38, '1'), (44, '0'), (46, '1'), (25, '1'), (51, '1'), (44, '0'), (40, '0'), (43, '1'), (51, '0'), (38, '1'), (46, '1'), (39, '1'), (45, '1'), (39, '0'), (26, '0'), (31, '0'), (53, '0'), (39, '0'), (46, '1'), (51, '1'), (53, '0'), (33, '1'), (32, '1'), (36, '0'), (41, '0'), (46, '1'), (52, '0'), (39, '1'), (46, '0'), (43, '0'), (32, '1'), (45, '0'), (40, '1'), (38, '0'), (41, '0'), (46, '1'), (55, '0'), (42, '0'), (37, '0'), (39, '0'), (37, '1'), (31, '1'), (65, '0'), (40, '0'), (54, '0'), (50, '0'), (38, '1'), (31, '0'), (34, '0'), (48, '1'), (35, '0'), (36, '0'), (32, '0'), (29, '0'), (48, '1'), (43, '0'), (46, '1'), (36, '1'), (43, '1'), (38, '1'), (35, '0'), (50, '1'), (30, '1'), (42, '0'), (41, '0'), (34, '1'), (58, '0'), (36, '1'), (35, '1'), (32, '0'), (53, '0'), (39, '1'), (47, '1'), (22, '0'), (36, '0'), (49, '0'), (44, '0'), (51, '0'), (36, '0'), (31, '0'), (44, '1'), (45, '0'), (39, '0'), (47, '0'), (39, '0'), (28, '1'), (42, '1'), (41, '0'), (55, '1'), (44, '1'), (48, '1'), (60, '0'), (45, '1'), (45, '0'), (50, '0'), (31, '0'), (39, '0'), (35, '1'), (35, '0'), (44, '0'), (36, '0'), (45, '0'), (40, '1'), (36, '0'), (38, '1'), (28, '0'), (45, '0'), (32, '1'), (28, '0'), (44, '0'), (35, '0'), (45, '0'), (31, '0'), (34, '1'), (30, '1'), (48, '0'), (56, '1'), (43, '1'), (42, '1'), (54, '0'), (44, '1'), (53, '0'), (41, '0'), (43, '0'), (42, '1'), (37, '1'), (44, '0'), (26, '1'), (34, '1'), (57, '1'), (34, '1'), (39, '0'), (51, '0'), (49, '0'), (41, '1'), (40, '1'), (39, '1'), (43, '0'), (34, '1'), (41, '0'), (38, '1'), (37, '0'), (39, '0')]
female_ages = untuple(result_female)

result_male = [(47, '0'), (45, '0'), (50, '1'), (40, '1'), (32, '1'), (39, '1'), (45, '1'), (44, '0'), (42, '0'), (28, '1'), (34, '1'), (46, '1'), (47, '0'), (38, '1'), (43, '0'), (50, '1'), (28, '1'), (41, '1'), (39, '1'), (56, '0'), (43, '0'), (42, '1'), (41, '0'), (36, '1'), (49, '0'), (19, '0'), (31, '0'), (32, '1'), (44, '0'), (48, '1'), (33, '0'), (44, '0'), (39, '0'), (48, '1'), (35, '1'), (39, '0'), (34, '0'), (53, '0'), (30, '1'), (40, '0'), (53, '1'), (50, '1'), (49, '0'), (43, '0'), (44, '1'), (52, '0'), (50, '0'), (45, '1'), (48, '1'), (33, '1'), (45, '1'), (32, '0'), (38, '0'), (38, '1'), (34, '0'), (44, '0'), (40, '1'), (48, '0'), (37, '1'), (42, '1'), (44, '1'), (24, '0'), (35, '1'), (43, '0'), (47, '0'), (56, '0'), (43, '0'), (49, '0'), (43, '0'), (28, '0'), (32, '1'), (41, '0'), (34, '0'), (45, '1'), (43, '0'), (37, '1'), (40, '0'), (38, '1'), (39, '0'), (51, '0'), (40, '1'), (34, '1'), (29, '1'), (34, '0'), (40, '1'), (28, '1'), (39, '1'), (44, '0'), (37, '0'), (42, '0'), (55, '1'), (56, '1'), (25, '0'), (56, '0'), (45, '1'), (42, '1'), (50, '1'), (39, '0'), (43, '1'), (38, '1'), (29, '1'), (35, '1'), (49, '0'), (39, '1'), (44, '1'), (34, '0'), (37, '0'), (37, '1'), (49, '1'), (33, '0'), (35, '1'), (39, '0'), (40, '0'), (46, '1'), (40, '1'), (57, '1'), (43, '0'), (52, '1'), (45, '0'), (55, '1'), (41, '0'), (31, '0'), (37, '0'), (39, '0'), (40, '0'), (48, '0'), (34, '0'), (37, '1'), (33, '0'), (32, '0'), (38, '1'), (29, '1'), (41, '1'), (36, '1'), (37, '1'), (30, '0'), (48, '1'), (37, '1'), (37, '1'), (36, '1'), (52, '1'), (42, '1'), (32, '1'), (45, '1'), (37, '1'), (28, '1'), (44, '1'), (32, '1'), (45, '1'), (49, '1'), (49, '1'), (43, '1'), (39, '0'), (43, '0'), (41, '1'), (30, '1'), (34, '0'), (34, '0'), (37, '0'), (48, '1'), (23, '1'), (48, '1'), (48, '1'), (45, '1'), (36, '1'), (30, '0'), (51, '0'), (58, '1'), (31, '1'), (47, '0'), (32, '0'), (48, '1'), (26, '1'), (39, '0'), (52, '0'), (42, '0'), (52, '1'), (35, '0'), (29, '1'), (35, '0'), (40, '0'), (33, '1'), (36, '0'), (34, '0'), (33, '0'), (46, '0'), (22, '0'), (36, '1'), (34, '0'), (32, '1'), (36, '1'), (38, '1'), (29, '1'), (40, '0'), (45, '0'), (37, '1'), (47, '0'), (33, '1'), (40, '1'), (43, '1'), (28, '0'), (33, '1'), (48, '0'), (26, '1'), (51, '1'), (23, '1'), (32, '1'), (41, '1'), (39, '0'), (47, '0'), (32, '1'), (42, '0'), (35, '1'), (39, '1'), (34, '1'), (34, '1'), (38, '1'), (43, '1'), (56, '1'), (37, '1'), (20, '1'), (32, '1'), (49, '1'), (44, '0'), (33, '0'), (47, '0'), (31, '1'), (40, '1'), (46, '0'), (29, '0'), (27, '0'), (41, '0'), (30, '1'), (41, '1'), (35, '1'), (36, '0'), (45, '0'), (41, '1'), (45, '0'), (34, '1'), (36, '0'), (21, '1'), (40, '1'), (43, '0'), (42, '1'), (29, '0'), (40, '0'), (40, '1'), (41, '0'), (38, '0'), (34, '0'), (41, '1'), (41, '0'), (32, '1'), (46, '1'), (45, '1'), (49, '0'), (28, '1'), (35, '0'), (37, '0'), (50, '1'), (29, '1'), (43, '1'), (50, '0'), (37, '1'), (29, '0'), (50, '0'), (52, '0'), (36, '1'), (33, '0'), (36, '1'), (39, '0'), (40, '1'), (47, '1'), (42, '0'), (25, '0'), (35, '0'), (37, '1'), (23, '1'), (37, '1'), (43, '0'), (39, '1'), (32, '0'), (48, '0'), (46, '1'), (39, '0'), (32, '1'), (32, '1'), (50, '1'), (30, '1'), (53, '0'), (20, '1'), (36, '0'), (37, '1'), (40, '1'), (37, '0'), (30, '1'), (49, '1'), (44, '0'), (44, '0'), (36, '1'), (40, '1'), (26, '0'), (38, '0'), (41, '1'), (29, '1'), (38, '1'), (43, '0'), (23, '1'), (39, '0'), (39, '1'), (28, '0'), (37, '0'), (39, '1'), (40, '0'), (41, '0'), (34, '0'), (22, '1'), (33, '1'), (23, '0'), (42, '0'), (32, '1'), (34, '0'), (45, '0'), (45, '1'), (46, '0'), (43, '1'), (45, '1'), (46, '0'), (29, '0'), (48, '1'), (29, '0'), (34, '0'), (44, '1'), (49, '0'), (47, '1'), (22, '1'), (40, '0'), (30, '0'), (33, '1'), (38, '0'), (47, '1'), (39, '0'), (35, '0'), (31, '0'), (30, '0'), (44, '0'), (28, '1'), (41, '0'), (36, '1'), (35, '0'), (54, '0'), (46, '0'), (32, '1'), (24, '0'), (28, '0'), (43, '0'), (38, '0'), (36, '0'), (39, '1'), (38, '1'), (42, '0'), (35, '1'), (42, '1'), (37, '1'), (13, '1'), (46, '0'), (32, '0'), (33, '1'), (46, '1'), (28, '1'), (22, '1'), (44, '1'), (55, '1'), (33, '0'), (33, '1'), (36, '0'), (39, '1'), (37, '1'), (46, '0'), (54, '1'), (40, '1'), (36, '0'), (29, '1'), (45, '1'), (45, '1'), (36, '1'), (52, '0'), (52, '1'), (29, '1'), (41, '0'), (53, '0'), (49, '0'), (40, '0'), (50, '0'), (41, '0'), (38, '0'), (33, '1'), (41, '0'), (39, '1'), (39, '0'), (35, '1'), (39, '0'), (47, '0'), (42, '0'), (38, '1'), (39, '0'), (58, '0'), (38, '0'), (45, '1'), (51, '0'), (41, '1'), (28, '1'), (43, '0'), (19, '0'), (47, '0'), (65, '0'), (32, '1'), (45, '1'), (35, '1'), (34, '0'), (44, '0'), (42, '0'), (34, '0'), (35, '1'), (35, '1'), (49, '0'), (41, '1'), (41, '0'), (46, '1'), (39, '1'), (27, '0'), (54, '1'), (42, '1'), (45, '0'), (28, '1'), (26, '0'), (49, '1'), (45, '0'), (54, '1'), (47, '0'), (40, '1'), (42, '1'), (35, '0'), (35, '1'), (39, '1'), (44, '1'), (48, '0'), (44, '0'), (54, '0'), (32, '1'), (40, '1'), (47, '1'), (47, '0'), (46, '0'), (46, '1'), (54, '1'), (36, '0'), (43, '0'), (24, '0'), (36, '1'), (38, '1'), (52, '0'), (36, '0'), (46, '1'), (36, '1'), (41, '0'), (36, '0'), (34, '1'), (49, '1'), (36, '0'), (40, '0'), (37, '1')]
male_ages = untuple(result_male)

result = ['2XL', '3XL', 'M', 'XS', 'S', '2XL', 'L', '2XL', '2XL', '2XL', 'S', '3XL', 'XS', 'L', 'L', '3XL', 'L', 'XL', 'XL', '3XL', 'XS', '2XL', 'XS', 'M', '2XL', 'XS', 'XS', '3XL', 'XS', 'L', '3XL', '3XL', 'S', 'L', 'XL', 'XL', 'S', '3XL', 'L', 'XS', 'XS', 'XS', 'XL', 'XS', 'L', '2XL', 'S', '3XL', 'L', 'S', 'S', 'XS', 'XS', 'XL', 'XL', '3XL', '2XL', '2XL', 'XL', 'XS', 'L', 'S', 'M', 'L', 'L', 'XL', '3XL', '2XL', '3XL', 'M', 'S', 'XS', '3XL', 'M', '2XL', '3XL', '3XL', '2XL', '3XL', 'L', '3XL', '2XL', 'L', 'XL', 'L', 'XS', 'XL', 'L', 'XS', 'L', 'XL', '2XL', '3XL', '2XL', 'L', 'L', 'M', 'L', '3XL', '2XL', 'S', '3XL', 'M', 'XL', 'S', 'S', 'XS', '3XL', 'S', '2XL', 'S', '3XL', 'S', 'S', '3XL', 'XL', 'M', 'XL', 'XS', 'XS', 'XL', 'M', 'S', '2XL', 'M', '2XL', 'L', '2XL', 'M', 'L', 'M', '2XL', 'M', 'L', '2XL', '3XL', 'XS', '3XL', 'XL', 'L', 'XS', '3XL', '2XL', 'L', 'M', 'XS', '2XL', 'S', 'XL', 'M', 'XL', 'S', '2XL', '2XL', 'M', 'M', '2XL', '2XL', 'XL', '2XL', '2XL', 'S', 'XS', '2XL', 'XS', 'XL', '2XL', 'XL', 'M', 'M', 'S', 'M', 'M', 'M', 'M', 'S', '2XL', 'M', 'L', 'XL', '3XL', 'S', 'M', 'XL', '2XL', 'S', 'S', '2XL', 'M', 'XS', 'XS', 'XS', 'XL', 'S', 'L', 'M', 'L', 'L', 'M', 'XS', '2XL', 'XS', 'S', '2XL', 'S', 'L', 'M', 'S', 'XS', '3XL', 'XL', 'S', 'L', '3XL', '2XL', 'XS', 'XL', 'XS', '3XL', 'XS', 'S', '2XL', 'L', 'S', 'M', '3XL', 'S', 'XS', '2XL', 'M', 'XL', 'S', '3XL', '3XL', 'XL', 'XS', 'L', '2XL', 'XL', 'XL', '2XL', '3XL', '3XL', '2XL', 'XS', '3XL', 'S', 'M', 'M', '2XL', 'M', 'XS', 'L', '2XL', 'XS', 'XS', '3XL', 'L', '2XL', 'XL', '2XL', '3XL', 'S', '3XL', 'M', 'M', 'XS', 'XS', '3XL', '2XL', 'XS', 'M', 'S', 'M', '3XL', '2XL', 'XL', 'M', 'XS', 'XL', 'M', '2XL', 'XL', '2XL', '3XL', 'XS', 'XS', 'L', '3XL', 'L', 'XS', 'M', 'XL', 'S', 'L', 'XS', 'S', 'XL', 'L', '2XL', '3XL', 'XS', 'S', 'XL', '3XL', 'XS', 'M', 'M', 'XL', 'M', 'S', 'S', '3XL', 'XS', 'S', 'XS', '2XL', 'XS', 'XS', 'XL', '3XL', 'XL', 'S', '2XL', '2XL', 'XL', 'L', 'XL', 'L', 'XS', 'XL', '2XL', '2XL', 'XS', 'XS', 'L', 'XL', 'XS', '2XL', 'XL', 'S', 'XS', '3XL', 'XS', 'L', 'S', 'M', '3XL', 'XL', 'S', 'XS', 'XS', '2XL', 'XS', 'S', 'M', 'M', '2XL', 'XL', 'M', 'XL', 'XS', '3XL', '2XL', 'L', 'XS', '3XL', 'M', 'XS', '3XL', '2XL', 'XS', '3XL', '3XL', '2XL', '3XL', 'S', 'M', 'XS', 'S', 'XS', 'L', '3XL', 'M', 'S', 'XS', 'S', 'L', '2XL', '3XL', 'XS', 'S', 'L', '2XL', '3XL', 'M', 'S', 'XL', 'XL', 'M', 'S', 'XL', 'L', 'XL', 'L', 'S', 'L', 'M', '2XL', 'XL', 'XS', 'XS', 'M', 'L', 'M', '3XL', 'S', 'S', 'S', '3XL', '2XL', 'XS', 'XL', 'M', 'M', 'XL', 'XL', 'L', 'XL', 'XS', 'XS', '3XL', 'XS', '3XL', '3XL', 'XS', 'S', 'XS', '3XL', '2XL', 'XS', 'S', 'S', 'M', 'S', 'XL', '2XL', 'XL', 'M', 'XS', '3XL', 'XS', 'L', '3XL', 'S', 'L', '2XL', 'M', '3XL', '2XL', 'S', 'M', 'XS', '3XL', 'S', 'S', '3XL', '2XL', 'XS', 'XL', 'L', 'M', 'XL', 'S', '2XL', 'M', '3XL', 'S', 'XS', '2XL', 'XS', '2XL', 'S', 'M', 'L', 'XL', '3XL', 'XS', 'XL', 'XL', 'L', 'L', 'XS', 'M', '3XL', '3XL', '3XL', 'M', '2XL', '2XL', 'M', '3XL', 'L', 'XL', 'S', '3XL', 'XL', '2XL', 'S', 'L', '2XL', 'XS', 'XL', '2XL', 'L', 'S', 'XL', 'M', 'S', '2XL', 'M', 'XS', 'XS', 'XL', 'XS', 'XL', '3XL', '2XL', 'S', 'L', 'M', 'S', 'L', '3XL', 'M', '2XL', 'L', '3XL', 'S', 'XS', 'S', '2XL', 'XS', 'XL', '2XL', 'S', 'M', '2XL', 'XL', 'XS', '2XL', '3XL', '2XL', 'XL', 'M', 'M', 'M', '3XL', 'S', 'XS', 'XS', 'XS', 'S', '2XL', '2XL', 'XS', 'M', 'XL', 'XS', 'S', 'M', 'XS', '2XL', 'M', 'XS', 'L', 'L', 'XL', 'XS', 'M', 'S', 'S', '2XL', 'S', 'L', '2XL', '3XL', 'M', 'M', 'M', 'XS', 'XS', 'L', 'S', '3XL', '3XL', 'M', 'S', 'XL', '2XL', 'M', 'S', 'S', 'M', '2XL', '3XL', 'M', 'S', '3XL', 'M', 'M', 'L', '3XL', '3XL', 'L', 'M', 'L', 'S', 'XS', 'XS', '3XL', 'XS', 'XL', 'S', '3XL', '2XL', 'M', 'XL', 'S', '2XL', 'XL', '2XL', 'L', 'S', 'S', 'M', 'L', 'XL', 'XL', '3XL', 'XS', '3XL', '2XL', 'S', 'L', 'XL', 'M', 'L', 'S', '2XL', 'M', 'XS', 'M', '2XL', 'XL', 'XS', '3XL', 'M', '2XL', 'L', 'L', '2XL', '2XL', 'L', '3XL', 'M', '2XL', 'XL', 'S', '2XL', 'XL', '3XL', '2XL', 'XS', 'M', 'L', 'L', 'L', 'XL', 'M', 'L', '2XL', '3XL', 'XL', 'XL', '3XL', '3XL', 'XS', '3XL', 'S', 'S', 'XL', 'L', '2XL', 'XL', 'L', '3XL', '3XL', 'XS', 'XL', 'XS', 'XL', '2XL', '3XL', 'XL', 'S', 'XS', '2XL', 'S', 'XS', 'M', '2XL', 'S', 'L', '3XL', 'S', 'XL', 'XL', 'M', 'M', 'L', 'M', 'XS', '2XL', 'XS', '3XL', 'M', '2XL', '2XL', 'L', 'M', 'XL', 'M', '3XL', 'S', '2XL', 'XS', 'M', 'S', 'L', '2XL', '3XL', 'M', '2XL', 'S', 'S', '2XL', '3XL', 'L', 'M', 'XS', 'XS', 'XS', '3XL', 'XS', 'S', '2XL', '3XL', '3XL', 'S', 'L', 'L', '2XL', 'M', 'L', 'L', 'XL', '3XL', 'M', 'S', 'M', 'XS', 'XS', 'L', 'L', 'M', 'S', 'XL', 'S', 'S', 'S', '3XL', '3XL', 'L', 'XL', 'XS', 'XL', 'XS', 'XS', 'M', 'M', '3XL', 'S', 'S', '2XL', 'L', '3XL', '2XL', '2XL', '2XL', 'M', '2XL', '3XL', 'XS', 'XS', 'XS', '2XL', 'L', 'XS', 'S', 'XS', '3XL', 'XL', 'S', 'M', '3XL', '2XL', 'XS', 'XS', 'M', 'S', 'XL', 'M', 'XS', 'M', 'XL', 'XL', 'XL', 'S', 'XS', '3XL', '2XL', 'XS', 'M', 'S', 'M', 'XS', 'XL', 'XL', '3XL', 'M', 'M', '2XL', 'L', 'S', 'XL', '3XL', 'M', 'XL', '2XL', 'XL', 'M', 'XS', '2XL', 'XS', 'XL', 'M', '3XL', 'XS', 'S', 'L', '3XL', 'XS', '3XL', 'S', 'L', '2XL', 'XL', 'XS', 'L', 'L', 'L', '2XL', 'S', 'L', 'S', 'S', '3XL', 'XL', 'XL', 'M', 'S', 'XS', 'L', 'S', '2XL', 'S', 'XL', 'L', '2XL', '2XL', 'M', 'L', '2XL', '3XL', 'S', 'XS', 'XS', '2XL', 'M', '3XL', 'M', 'XS', 'S', 'S', 'XS', '3XL', 'M', '2XL', '2XL', 'L', '3XL', 'L', 'XS', 'M', 'L', '2XL', 'XL', 'L', 'XS', 'XS', 'L', 'L', 'L', 'XL', 'XS', 'XL', 'M', '3XL', 'XL', '2XL', '3XL', 'M', 'S', 'S', '3XL', 'S', '2XL', 'XS', '3XL', '3XL', 'XS', 'M', 'M', 'XS', 'M', 'L', 'XS', '3XL', '2XL', 'S', 'L', 'S', 'XS', 'S', 'S', 'M', 'XL', '2XL', '2XL', 'L', '2XL', 'M', 'XL', 'XS', 'XL', 'M', 'M', '3XL', 'M', 'XS', 'L', '2XL', 'M', 'M', '3XL', 'L', '2XL', '2XL', 'XS', 'L', 'L', '3XL', 'XL', '2XL', '2XL', 'S', 'XL', 'L', 'XS', '3XL', 'S', 'L', 'XS', '2XL', 'S', 'S', '3XL', 'S', 'L']
size_result = Counter(result)
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

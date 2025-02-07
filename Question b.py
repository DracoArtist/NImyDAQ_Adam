import json
import matplotlib.pyplot as plt
import numpy as np
from my_classes.statistics_file import Statistics

with open(r'Adam\Complete_adam_results.json', 'r') as json_file:
    content = json.load(json_file)

data = content['data']
# x_range = [i for i in range(len(data))]
# y_range = [float(data[i]) for i in x_range]


# Faire l'histogramme
histogram_dict = {}

for point in data:
    point = float(point)
    try:
        histogram_dict[point] +=1
    except:
        histogram_dict[point] = 1

x_range = sorted(list(histogram_dict.keys()))

# y_range = [histogram_dict[i] for i in x_range]

# plt.plot(x_range, y_range, 'o', markersize=5)
# plt.ylabel('Nombre de mesures')
# plt.xlabel('Tension mesurée (V)')
# plt.xticks(ticks=x_range)
# plt.grid(visible=True, which='major', ls=':')
# plt.tick_params(top=True, right=True, labeltop=True, labelright=True)
# plt.show()




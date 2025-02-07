import json
import matplotlib.pyplot as plt
import numpy as np
from my_classes.statistics_file import Statistics

stat = Statistics()

with open(r'Adam\Complete_adam_results.json', 'r') as json_file:
    content = json.load(json_file)

data = content['data']

mean, std = stat.compute_mean_and_deviation(data)

type_b = 3.245639 * 10**(-4) / (12**0.5)

N_min = (std / ((1.1**2 - 1)**0.5 * type_b)) **2

R2 = 100*mean / (2-mean)

print(mean)
print(R2)
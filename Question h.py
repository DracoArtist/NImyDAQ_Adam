import json
from my_classes.statistics_file import Statistics

stat = Statistics()

with open(r'Adam\Complete_adam_results.json', 'r') as json_file:
    content = json.load(json_file)

data = content['data']

mean, std = stat.compute_mean_and_deviation(data)

alpha_V2 = ((std / (len(data)**0.5))**2 + 0.0001**2)**0.5
alpha_V1 = 0.009
V1 = 2

relative_R1 = 0.05

R2 = 10801.332

uncertainty = R2*(relative_R1**2 + (alpha_V2 / mean)**2 + ((alpha_V2**2 + alpha_V1**2)**0.5 / (2-mean))**2)**0.5

print(f'{uncertainty: .12f}')
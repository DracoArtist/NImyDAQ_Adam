import json
from my_classes.statistics_file import Statistics
from sympy import symbols, diff

"""
Calcul l'incertitude pour la question h
"""

stat = Statistics()

with open(r'Adam\Complete_adam_results.json', 'r') as json_file:
    content = json.load(json_file)

data = content['data']

mean, std = stat.compute_mean_and_deviation(data)

R1 = symbols('R1')
V2 = symbols('V2')
Vt = symbols('Vt')
u_R1 = symbols('u_R1')
u_V2 = symbols('u_V2')
u_Vt = symbols('u_Vt')

R2 = R1*V2 / (Vt-V2)

u_R2 = ( (diff(R2, R1)*u_R1)**2 +  (diff(R2, V2)*u_V2)**2 + (diff(R2, Vt)*u_Vt)**2)**0.5

print(
    u_R2.evalf(subs={
        R1:100,  # R1 c'est la résistance de 100 ohm
        V2:mean,  # V2 c'est la tension mesuré
        Vt:2,  # Vt c'est la tension totale de 2V
        u_R1:5,  # l'incertitude sur R1 c'est 0.05*100 = 5 ohm
        u_V2:0.00009369,  # On néglige l'incertitude de type A
        u_Vt:0.009  # Incertitude donnée par le fabriquant
    })
)
import numpy as np
from sympy import symbols

"""
Retourne les constantes fondamentales composant le ohm en utilisant de l'algèbre linéaire!
"""


A = np.matrix([
    [0,1,2,0,2,0],
    [-1,-1,-1,1,-2,0],
    [0,0,1,0,1,0],
    [0,0,0,1,0,0],
    [0,0,0,0,-1,0],
    [0,0,0,0,0,-1]
])

A_1 = np.linalg.inv(A)

ohm = np.array([2,-3,1,-2,0,0]).reshape(6,1)

ohm_vector = A_1.dot(ohm)

v_Cs = symbols('v_Cs')  # Fréquence de transition du 133CS
c = symbols('c')  # Vitesse de la lumière
h = symbols('h')  # Constante de Planck
e = symbols('e')  # Charge élémentaire
kB = symbols('kB')  # Constante de Boltzman
Na = symbols('Na')  # Nombre d'Avogadro

ohm = v_Cs**ohm_vector[0,0]*c**ohm_vector[1,0]*h**ohm_vector[2,0]*e**ohm_vector[3,0]*kB**ohm_vector[4,0]*Na**ohm_vector[5,0]

print(ohm)

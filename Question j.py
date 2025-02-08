import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Permet de tracer le graphique avec la regression linéaire pour la question j)
Print l'équation de la droite et les incertitudes
"""

csv_file = pd.read_csv(r'Adam\Adam_data.csv')  # Mettre le file_path vers son csv

V1_list = csv_file['Reference Voltage']
V2_list = csv_file['Unknown Voltage']
Current = csv_file['Current']

resolution = 9.369354 * 10**(-5)
R1_relative_uncertainty = 0.05

error_list = []

for i in range(len(V1_list)):
    V1 = V1_list[i]
    V2 = V2_list[i]
    current_Rerror = ((resolution / V1)**2 + R1_relative_uncertainty**2)**0.5
    error = ((V2 * current_Rerror)**2 + resolution**2)**0.5
    error_list.append(error)

V1_list = np.array(V1_list)
V2_list = np.array(V2_list)
Current = np.array(Current)
error_list = np.array(error_list)
weight = 1/(error_list**2)

delta = sum(weight) * np.dot(weight, Current**2) - (np.dot(weight, Current))**2
slope = (sum(weight) * sum(weight * V2_list * Current) - np.dot(weight, V2_list) * np.dot(weight, Current)) / delta
origin = (np.dot(weight, Current**2) * np.dot(weight, V2_list) - np.dot(weight, Current) * sum(weight * V2_list * Current)) / delta

d_origin = (np.dot(weight, Current**2) / delta)**0.5
d_slope = (sum(weight) / delta)**0.5
print(d_origin, d_slope)


# Plotting
## General plot
x_range = [i*1000 for i in Current]

plt.ylabel('Voltage (V)')
plt.xlabel('Courant (mA)')
plt.grid(visible=True, which='major', ls=':')
plt.tick_params(top=True, right=True, labeltop=True, labelright=True)
plt.ylim(0,10)
plt.xlim(0,0.9)
print(f"""
    V = {slope: .2e} * I + {abs(origin): .2f}
    Incertitude sur la pente de {d_slope:.0e}
    Incertitude sur l'origine de {d_origin:.2f}
    """
)

## Plot data
plt.errorbar(
    x=x_range,
    y=V2_list,
    yerr=error_list,
    capsize=3,
    marker='o',
    markersize=3,
    markeredgecolor='black',
    markerfacecolor='black',
    ecolor='black',
    ls='none',
    zorder=2,
)

## Plot regression
y_range = [(slope*i + origin) for i in Current]
plt.plot(x_range, y_range, '#fc039d', zorder=3, linewidth=1.5)
plt.fill_between(
    x=x_range, 
    y1=(slope + d_slope) * Current + (origin + d_origin),
    y2=(slope - d_slope) * Current + (origin - d_origin),
    zorder=1,
    alpha=0.5
)


plt.show()


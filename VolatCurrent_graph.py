import matplotlib.pyplot as plt
import csv
import numpy as np

# Définir les variables globales
current_range = []
voltage_range = []
y_error_range = [[],[]]

# Extraires les données du CSV
with open(r"Adam\Adam_data.csv", 'r') as data_file:
    reader = csv.reader(data_file)
    next(reader)
    for row in reader:
        current_range.append(float(row[-2]) * 1000)
        voltage_range.append(float(row[2]))
        y_error_range[0].append(float(row[3]))
        y_error_range[1].append(float(row[3]))

# Convertir pour calcul plus simples
current_range_array = np.array(current_range)
voltage_range_array = np.array(voltage_range)

# Calculer la droite de régression
N = len(current_range_array)
current_average = sum(current_range_array) / N
delta = N*sum([(i-current_average)**2 for i in current_range_array])

slope = (
    N*np.dot(current_range_array, voltage_range_array) 
    - sum(current_range_array) * sum(voltage_range_array)
    ) / delta

origin = (
    sum([i**2 for i in current_range_array]) * sum(voltage_range_array)
    - sum(current_range_array) * np.dot(current_range_array, voltage_range_array) 
    ) / delta

regression_range = np.linspace(0,9,100)

def regression(x):
    return origin + x*slope


# Faire le graphique
## Mettre les données
plt.plot(regression_range, regression(regression_range))
plt.errorbar(current_range, voltage_range, xerr=y_error_range, capsize=3, ecolor = "black", fmt="none", linestyle='')

## Mettre le text
plt.ylabel("Tension aux bornes de la résistance inconnue (V)")
plt.xlabel("Courant passant dans le circuit (mA)")

plt.text(
    x = 0.05,
    y = 8,
    s = f"Regression: V = {slope: .3f}*I {origin: .3f}",
    snap=True
)

## Gérer les graduations
yticks = np.linspace(0, 9, 10)
yticks_labels = [f'{i: .3}' for i in yticks]
plt.yticks(ticks=yticks, labels=yticks_labels)

plt.xlim(0, 0.9)
plt.ylim(0, 9)

plt.tick_params(top=True, right=True, labeltop=True, labelright=True)

plt.grid(visible=True, which='major', ls=':')

## Afficher le graphique
plt.show()

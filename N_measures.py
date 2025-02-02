from classes.statistics_file import Statistics
from classes.myDAQmeasures import Measure, DataShelf
import matplotlib.pyplot as plt
import csv

# Set up les classes nécessaires
datashelf = DataShelf()  # Data holder
measure = Measure(datashelf=datashelf)
statistics = Statistics()

# Setup les informations générales
channel_voltage_ouput = "moduleD/ao0"
reference_voltage_measure = "tempSensor1/ai0"  # Channel lié à la résistance connue
unknonw_voltage_measure = "tempSensor1/ai1"  # Channel lié à la résistance inconnue
voltage = 2
voltage_step = 0.4
measure.sample_count = 10  # nombre de points pris par mesures
reference_resistance = 100  # Ohm
number_of_measures = 40

# Prendre n mesures
measure.n_series_of_measure(
    n=number_of_measures,
    initial_voltage=voltage,
    voltage_step=voltage_step,
    voltage_output_channel=channel_voltage_ouput,
    known_resistor_channels=reference_voltage_measure,
    unknown_resistor_channel=unknonw_voltage_measure
)


# Faire un graphique avec les moyennes des données recueuillis
voltage_range = []
current_range = []

for i in range(number_of_measures):
    data = getattr(datashelf, f"measurment{i}")
    
    statistics.compute_mean_and_deviation(data[0])

    reference_resistance_voltage = statistics.mean

    current = statistics.compute_current(voltage=reference_resistance_voltage, resistance=reference_resistance)
    current_range.append(current)

    statistics.compute_mean_and_deviation(data[1])

    unknown_resistance_voltage = statistics.mean
    voltage_range.append(unknown_resistance_voltage)

plt.plot(voltage_range, current_range, 'o')
plt.show()

# Mettre les données dans un csv
with open(r"TP_Mesure_resistance\data.csv", 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Voltage', 'Current'])
    for volt, current in zip(voltage_range, current_range):
        writer.writerow([volt, current])

# - 

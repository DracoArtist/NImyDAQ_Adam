from my_classes.statistics_file import Statistics
from my_classes.myDAQmeasures import Measure, DataShelf
import matplotlib.pyplot as plt
import csv

# Set up les classes nécessaires
datashelf = DataShelf()  # Data holder
measure = Measure(datashelf=datashelf)
statistics = Statistics()

# Setup les informations générales
channel_voltage_ouput = "DAQ_team_3_PHS2903/ao0"
reference_voltage_measure = "DAQ_team_3_PHS2903/ai0"  # Channel lié à la résistance connue
unknonw_voltage_measure = "DAQ_team_3_PHS2903/ai1"  # Channel lié à la résistance inconnue
initial_voltage = 1
voltage_step = 0.2
measure.sample_count = 1000  # nombre de points pris par mesures
reference_resistance = 100  # Ohm
number_of_measures = 40

# Prendre n mesures
measure.n_series_of_voltage_measure(
    n=number_of_measures,
    initial_voltage=initial_voltage,
    voltage_step=voltage_step,
    voltage_output_channel=channel_voltage_ouput,
    known_resistor_channels=reference_voltage_measure,
    unknown_resistor_channel=unknonw_voltage_measure
)


# Faire un graphique avec les moyennes des données recueuillis
reference_voltage_range = []
reference_voltage_uncertainty_range = []
unknown_voltage_range = []
unknown_voltage_uncertainty_range = []
current_range = []
resistance_range = []

for i in range(number_of_measures):
    data = getattr(datashelf, f"measurment{i}")
    
    reference_resistance_voltage, reference_resistance_voltage_deviation = statistics.compute_mean_and_deviation(data[0])
    reference_voltage_range.append(reference_resistance_voltage)
    reference_voltage_uncertainty_range.append(reference_resistance_voltage_deviation)

    current = statistics.compute_current(voltage=reference_resistance_voltage, resistance=reference_resistance)
    current_range.append(current)

    unknown_resistance_voltage, unknown_resistance_voltage_deviation = statistics.compute_mean_and_deviation(data[1])
    unknown_voltage_range.append(unknown_resistance_voltage)
    unknown_voltage_uncertainty_range.append(unknown_resistance_voltage_deviation)

    unknown_resistance = statistics.compute_resistance(voltage=unknown_resistance_voltage, current=current)
    resistance_range.append(unknown_resistance)


# Mettre les données dans un csv
with open(r"data.csv", 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([
        'Reference Voltage',
        'Reference Voltage std',
        'Unknown Voltage',
        'Unknown Voltage std',
        'Current',
        'Resistance'])
    for volt_k, std_k, volt_u, std_u, current, resistance in zip(
        reference_voltage_range,
        reference_voltage_uncertainty_range,
        unknown_voltage_range,
        unknown_voltage_uncertainty_range,
        current_range,
        resistance_range):
        writer.writerow([volt_k, std_k, volt_u, std_u, current, resistance])



# plt.plot(unknown_voltage_range, current_range, 'o')
# plt.xlabel("Tension aux bornes de la résistance inconnue")
# plt.ylabel("Courant passant dans le circuit")
# plt.show()
# # - 

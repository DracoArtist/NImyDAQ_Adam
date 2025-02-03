from my_classes.statistics_file import Statistics
from my_classes.myDAQmeasures import Measure
import json

measure = Measure()  # Initialisation de la classe measure qui va prendre les mesures et faire les graphiques

# Déclaration des variables globales
channel_voltage_ouput = "DAQ_team_3_PHS2903/ao0"
channel_voltage_measure = "DAQ_team_3_PHS2903/ai1"
voltage = 2
measure.sample_count = 1000  # nombre de points pris par mesures

# Générer un voltage
measure.write_voltage(
    voltage=2,
    channel=channel_voltage_ouput
)

# Prendre les 1000 mesures
measure.read_voltage(channel_voltage_measure)

# Faire le graphique
x_range = [i+1 for i in range(1000)]
data = measure.data

measure.plot_data(x_range, data)

# Calculer la moyenne et l'écart-type
statistics = Statistics()

statistics.compute_mean_and_deviation(data)
print(f"""
      Les données préliminaire ont été prises avec {measure.sample_count} points.
      La moyenne des mesures préliminaires est {statistics.mean}.
      L'écart-type des mesures préliminaires est {statistics.standard_deviation}
""")

with open(r"results.json", 'a') as json_file:
    text = {
        'Analyse preliminaire':{
            'Nombre de point': measure.sample_count,
            'Moyenne': statistics.mean,
            'Ecart-type': statistics.standard_deviation
        }
    }
    json.dump(text, json_file, indent=2)


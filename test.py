import nidaqmx
from nidaqmx.constants import AcquisitionType, VoltageUnits
from my_classes.statistics_file import Statistics
import csv

statistics = Statistics()

voltage_range = []
reference_voltage_range = []
current_range = []
resistance_range = []
known_resistance_range = []

for i in range(10):
    voltage = 2.0 + i*0.4

    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan("DAQ_team_3_PHS2903/ao0", units=VoltageUnits.VOLTS)
        task.write(voltage)

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("DAQ_team_3_PHS2903/ai0")
        task.ai_channels.add_ai_voltage_chan("DAQ_team_3_PHS2903/ai1")
        task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)
        data = task.read(number_of_samples_per_channel=2)
        print(data)


        reference_resistance_voltage = statistics.compute_mean_and_deviation(data[0])[0]
        reference_voltage_range.append(reference_resistance_voltage)

        current = statistics.compute_current(voltage=reference_resistance_voltage, resistance=100)
        current_range.append(current)

        known_resistance = statistics.compute_resistance(voltage=reference_resistance_voltage, current=current)
        known_resistance_range.append(known_resistance)

        unknown_resistance_voltage = statistics.compute_mean_and_deviation(data[1])[0]
        voltage_range.append(unknown_resistance_voltage)

        unknown_resistance = statistics.compute_resistance(voltage=unknown_resistance_voltage, current=current)
        resistance_range.append(unknown_resistance)

# with nidaqmx.Task() as task:
#     task.ao_channels.add_ao_voltage_chan("DAQ_team_3_PHS2903/ao0", units=VoltageUnits.VOLTS)
#     task.write(4)

# with nidaqmx.Task() as task:
#     task.ai_channels.add_ai_voltage_chan("DAQ_team_3_PHS2903/ai0")
#     task.ai_channels.add_ai_voltage_chan("DAQ_team_3_PHS2903/ai1")
#     task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)
#     data = task.read(number_of_samples_per_channel=1000)

#     reference_resistance_voltage = statistics.compute_mean_and_deviation(data[0])[0]
#     reference_voltage_range.append(reference_resistance_voltage)

#     current = statistics.compute_current(voltage=reference_resistance_voltage, resistance=100)
#     current_range.append(current)

#     known_resistance = statistics.compute_resistance(voltage=reference_resistance_voltage, current=current)
#     known_resistance_range.append(known_resistance)

#     unknown_resistance_voltage = statistics.compute_mean_and_deviation(data[1])[0]
#     voltage_range.append(unknown_resistance_voltage)

#     unknown_resistance = statistics.compute_resistance(voltage=unknown_resistance_voltage, current=current)
#     resistance_range.append(unknown_resistance)

with open(r"data.csv", 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Unknown Voltage','Known voltage', 'Current', 'Unknown Resistance', 'Known Resistance'])
    for k_volt, u_volt, current, u_resistance, k_resistance in zip(voltage_range, reference_voltage_range, current_range, resistance_range, known_resistance_range):
        writer.writerow([k_volt, u_volt, current, u_resistance, k_resistance])

print('File finished running')
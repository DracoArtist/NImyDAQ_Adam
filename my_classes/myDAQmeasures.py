import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, VoltageUnits
import matplotlib.pyplot as plt

class Measure:
    def __init__(self, sample_count: int = 1000, datashelf = 'optional'):
        self.sample_count = sample_count
        self.datashelf = datashelf


    def write_voltage(self, voltage: float, channel : str = 'DAQ_team_3_PHS2903/ao0'):
        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(channel, units=VoltageUnits.VOLTS)
            task.write(2.0)

    def read_voltage(self, *args):
        channels = args

        with nidaqmx.Task() as task:

            for channel in channels:
                task.ai_channels.add_ai_voltage_chan(channel)

            task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)
            data = task.read(number_of_samples_per_channel=self.sample_count)
            self.data = data

    def n_series_of_voltage_measure(self, n:int, initial_voltage: float, voltage_step: float, voltage_output_channel, known_resistor_channels, unknown_resistor_channel):

        assert self.datashelf.__class__ == DataShelf, "ERROR: <Measure> does not contain DataShelf"

        for i in range(n):
            self.write_voltage(voltage=initial_voltage+i*voltage_step, channel=voltage_output_channel)
            self.read_voltage(known_resistor_channels, unknown_resistor_channel)

            setattr(self.datashelf, f"measurment{i}", self.data)



    def plot_data(self, x_range, *args):  # args are lists of the data (y_values) 
        for data_list in args:
            plt.plot(x_range, data_list)
        
        plt.show()

class DataShelf:
    def __init__(self):
        pass
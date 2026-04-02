import matplotlib.pyplot as plot
import numpy as npy

def create_example_graphs():
    voltage = [(0.1 * num) for num in range(0, 50)]
    power = []
    current = []

    for num in voltage:
        power.append(-0.01 * (num ** 5) + 0.65 * (num ** 2))
        current.append(-1 * (8 ** (num - 3.6)) + 2.5)
    current.pop()
    current.append(0)
    
    return voltage, power, current

def graph_data(voltage, power, current):
    max_pow = npy.max(power)
    max_ind = power.index(max_pow)
    max_volt = voltage[max_ind]
    max_curr = current[max_ind]

    zero = current.index(0) * 0.1

    plot.figure(figsize = (10, 8))
    plot.plot(voltage, power, label = "Power (W)")
    plot.plot(voltage, current, label = "Current (A)")

    plot.grid(True, alpha = 0.3, linestyle = ':')
    plot.ylim(0, max_pow + 0.5)
    plot.xlim(0, zero)

    plot.title("Power & Current Over Voltage")
    plot.xlabel("Voltage (V)")
    plot.legend()

    return max_pow, max_volt, max_curr

volt, powr, curr = create_example_graphs()
print(graph_data(volt, powr, curr))
plot.show()
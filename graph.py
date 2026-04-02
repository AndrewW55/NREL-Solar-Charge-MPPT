import matplotlib.pyplot as plot
import numpy as npy

voltage = [(0.1 * num) for num in range(0, 50)]
power = []
current = []

for num in voltage:
    power.append(-0.01 * (num ** 5) + 0.65 * (num ** 2))
    current.append(-1 * (8 ** (num - 3.6)) + 2.5)

plot.figure(figsize = (10, 8))
plot.plot(voltage, power)
plot.plot(voltage, current)

plot.grid(True, alpha = 0.3, linestyle = ':')
plot.ylim(0, 4)
plot.xlim(0, 5)

max_pow = npy.max(power)
print(max_pow)
max_ind = power.index(max_pow)
print(max_ind)
max_volt = voltage[max_ind]
print(max_volt)
max_curr = current[max_ind]
print(max_curr)

plot.show()
import csv
import matplotlib.pyplot as plt

with open('logs_0408.csv', newline='') as csvfile:
    measurements = list(csv.reader(csvfile, delimiter=','))

times = [7]
#for m in measurements:
    #times.append(int(m[1]))

for m in range(1, len(measurements)):
    if int(measurements[m][1]) > int(measurements[m-1][1]):
        times.append(times[-1] + (int(measurements[m][1]) - int(measurements[m-1][1])))
    else:
        times.append(times[-1] + int(measurements[m][1]))

frequency = []
for_graph = []
for array_index in range(7, times[-1]):
    for_graph.append(array_index)
    try:
        times.index(array_index)
        frequency.append(1)
    except:
        frequency.append(0)
        continue

plt.plot(for_graph[0: 400], frequency[0: 400])
plt.ylabel('1: Received / 0: not-received data')
plt.xlabel('Time (in seconds)')
plt.show()

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

board_temperature = []
light_blue = []
light_red = []
room_temp = []
for m in measurements:
    board_temperature.append(float(m[2]))
    light_blue.append(float(m[3]))
    light_red.append(float(m[4]))
    room_temp.append(0.0685*float(m[5])-27.2)

""" 

# Plot of board temperature

plt.scatter(times, board_temperature)
plt.ylabel('Temperature in degrees of Celsius')
plt.xlabel('Time (in seconds)')
plt.show() """

""" 

# Plot of light levels

fig, ax = plt.subplots()
ax.plot(times, light_blue, label="Blue channel")
ax.plot(times, light_red, label="Red channel")
ax.legend()
plt.ylabel('Light level')
plt.xlabel('Time (in seconds)')
plt.show() """

# Plot of room temperature

plt.plot(times, room_temp)
plt.ylabel('Temperature in degrees of Celsius')
plt.xlabel('Time (in seconds)')
plt.show()
import time
import serial
import collections

ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port

x_coords = collections.deque([0. for i in range(20)], maxlen=20)
y_coords = collections.deque([0. for i in range(20)], maxlen=20)
z_coords = collections.deque([0. for i in range(20)], maxlen=20)

while True:
    #print(ser.readline()) # Read the newest output from the Arduino

    coord_str = ser.readline().decode()
    coords = coord_str.split()
    x_coords.append(float(coords[1]))
    y_coords.append(float(coords[3]))
    z_coords.append(float(coords[5]))

    delta_y1 = y_coords[19] - y_coords[18]
    delta_y2 = y_coords[18] - y_coords[17]

    #print(coord_str)

    #print(str(y_coords[19]) + ' ' + str(z_coords[19]))

    #print('.')
    #print(str(y_coords[i]) + ' ' for i in range(15,19))

    if (y_coords[18] - y_coords[19]) > 3 and (z_coords[18] - z_coords[19]) > 3:
        print('Thank you')

    elif abs(x_coords[18] - x_coords[19]) > 3 and (y_coords[18] - y_coords[19]) > 3:
        print('Hello')


    time.sleep(.5)  # Delay for one fifth of a second

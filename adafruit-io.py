import time
import serial
import collections

ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port

x_coords = collections.deque([0. for i in range(20)], maxlen=20)
y_coords = collections.deque([0. for i in range(20)], maxlen=20)
z_coords = collections.deque([0. for i in range(20)], maxlen=20)

resistance1 = collections.deque([0. for i in range(20)], maxlen=20)
resistance2 = collections.deque([0. for i in range(20)], maxlen=20)


x_thresh = 3
y_thresh = 3
z_thresh = 3

res_thresh1 = -1500
res_thresh2 = -900
t=0

while True:
    #print(ser.readline()) # Read the newest output from the Arduino

    coord_str = ser.readline().decode()

    coords = coord_str.split()

    x_coords.append(float(coords[1]))
    y_coords.append(float(coords[3]))
    z_coords.append(float(coords[5]))
    resistance1.append(float(coords[7]))
    resistance2.append(float(coords[9].strip('\r\n')))

    delta_y1 = y_coords[19] - y_coords[18]
    delta_y2 = y_coords[18] - y_coords[17]

    if (y_coords[18] - y_coords[19]) > y_thresh and (z_coords[18] - z_coords[19]) > z_thresh:
        print('Thank you')

    elif abs(x_coords[18] - x_coords[19]) > x_thresh and (y_coords[18] - y_coords[19]) > y_thresh:
        print('Hello')

    thresh1 = (resistance1[19] - resistance1[17] < res_thresh1)
    thresh2 = (resistance2[19] - resistance2[17] < res_thresh2)

    if thresh1 and not thresh2:
        print("A")
    elif not thresh1 and thresh2:
        print("B")
    # elif thresh1 and thresh2:
    #     print("C")

    t+=1
    # Loop for 50 iterations
    if t>50:
        break

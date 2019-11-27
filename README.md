# Graphene-enhanced motion sensor gloves for gesture-to-text recognition

This project, and all accompanying code, was completed in 24 hours during the [Graphene Hackathon](https://www.graphenehackathon.com/) hosted by the GEIC in Manchester, UK. It is rudimentary and admittedly would perform very poorly in any real world situation; however, it sufficed as a proof-of-concept in the judging stage of the event, for which we won first prize and the innovation prize. 

Everything created at the event is in the public domain and free to use. This code is simplistic but it may serve to inform other hackers/enthusiasts about the process we used to create this project. 

## First steps
For this project we used the [Adafruit Flora](https://learn.adafruit.com/) and the [LSM303 accelerometer](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout) to measure the change in position and orientation of the glove. In order to upload a project to the Flora it is necessary to first install the [Arduino IDE](https://www.arduino.cc/en/Main/Software) and additional [Adafruit libaries](https://learn.adafruit.com/flora-accelerometer/downloads). 

To run the python code with conditional motion interpretation, we installed the library (pySerial)[https://github.com/pyserial/pyserial], which allows the script to read from the Flora's port on the laptop. 

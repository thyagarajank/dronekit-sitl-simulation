# Simulating Drone Operations with SITL and DroneKit
Explore the world of drone development with this comprehensive guide to setting up and testing drone operations using SITL (Software In The Loop) simulation and DroneKit. This repository provides step-by-step instructions for installing and configuring the necessary software components, creating a virtual environment with Anaconda, and installing essential packages such as DroneKit, pymavlink, and MAVProxy. Learn how to run basic tests to ensure proper installation and functionality, set up a simulated vehicle with SITL, and interact with a Ground Control Station (GCS) using Mission Planner. Dive into testing patterns and explore circular flight patterns, arm and takeoff sequences, and return-to-launch procedures. Whether you're a novice or an experienced developer, this repository is your gateway to mastering drone development in a simulated environment.

# Introduction
In this project, I'll guide you through setting up DroneKit Python on Windows. The DroneKit-Python can be installed on a Linux, Mac OSX, or Windows computer that has Python 3.6 to 3.11 and can install Python packages from the Internet.

### Step 1. Anaconda Installation
 You can find the Anaconda distribution repository at https://repo.anaconda.com/archive/.
Download and install Anaconda: Make sure to download the “Python 3.7 to 3.11 Version” for the appropriate architecture.

### Step 2. Creating a virtual environment on Anaconda
```
conda create -n drone python=3.6.13
```

### Step 3. Dronekit Importent Packages Version
(Use Python 3.6 to 3.11 Version)
dronekit: This is the core package for interfacing with drones using Python.
```
pip install dronekit==2.9.2
```
pymavlink: It's a low-level Python interface to MAVLink messages.
```
pip install pymavlink==2.4.2
```
MAVProxy: This is a command-line ground station software framework used for drone development.
```
pip install mavproxy==1.8.46
```
### Step 4. Install Other Requirements Packages

```
pip install -r requirements.txt
```
### Step 5. Basic “Hello Drone” Check the Installation
The script below first launches the simulator. It then imports and calls the connect() method, specifying the simulator’s connection string (tcp:127.0.0.1:5760). The method returns a Vehicle object that we then use to query the attributes.
```
python hello.py
```
You should see the following output from the simulated vehicle:

```
Start simulator (SITL)
Downloading SITL from http://dronekit-assets.s3.amazonaws.com/sitl/copter/sitl-win-copter-3.3.tar.gz
Extracted.
Connecting to vehicle on: 'tcp:127.0.0.1:5760'
>>> APM:Copter V3.3 (d6053245)
>>> Frame: QUAD
>>> Calibrating barometer
>>> Initialising APM...
>>> barometer calibration complete
>>> GROUND START
Get some vehicle attribute values:
 GPS: GPSInfo:fix=3,num_sat=10
 Battery: Battery:voltage=12.587,current=0.0,level=100
 Last Heartbeat: 0.713999986649
 Is Armable?: False
 System status: STANDBY
 Mode: STABILIZE
Completed
```
That’s it- you’ve run your first DroneKit-Python script.

### Step 6. Setting up a Simulated Vehicle (SITL)
SITL (Software In The Loop) simulator allows you to create and test DroneKit-Python apps without a real vehicle (and from the comfort of your own developer desktop!).
#### Installation
The tool is installed (or updated) on all platforms using the command:
```
pip install dronekit-sitl -UI
```
### Step 7. Running SITL.
To run the latest version of Copter (e.g. “quad”), for which we have binaries (downloading the binaries if needed), you can simply call:
Default home location
```
dronekit-sitl copter
```
### or
Copter with set Home Location gps coordinates(Latitude and longitude coordinates are: 13.067439, 80.237617)
```
dronekit-sitl copter --home=13.0627621,80.2788886,584,353
```
### Run Setup For Plane Model (Optional)

Plane Model(e.g.: Flight or Fixed Wing)
```
dronekit-sitl plane-3.3.0 --home=13.0627621,80.2788886,584,353
```
### Other Useful Arguments (Optional)
There are a number of other useful arguments:
```
dronekit-sitl -h            #List all parameters to dronekit-sitl.
dronekit-sitl copter -h     #List additional parameters for the specified vehicle (in this case "copter").
dronekit-sitl --list        #List all available vehicles.
dronekit-sitl --reset       #Delete all downloaded vehicle binaries.
dronekit-sitl ./path [args...]  #Start SITL instance at target file location.
```
### Step 8. GCS Setup.
Open Mission Planner Ground Control Station (GCS) Software. https://ardupilot.org/planner/docs/mission-planner-installation.html
```
Select Connection: TCP
Enter Host Name/IP: 127.0.0.1
Enter Remote Port: 5760
```
### Step 9. Run SITL.
Open another Anaconda Prompt window, Run ARM-test and Takeoff-RTL-test Python Program.
```
python Arm-test.py
```
```
python Takeoff-RTL-Test.py
```
The SITL (Software In The Loop) drone is flying at an altitude of 20 meters. The drone program runs without any errors, indicating that it is functioning correctly and is ready to proceed to the next step.

### Step 9. Testing Pattern.
Simulated vehicle, arms it, commands it to take off to a specified altitude, flies it in a circular pattern, and then returns it to the launch (home) location.
```
python circular-pattern.py
```

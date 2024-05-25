from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import math

# Connect to the Vehicle (in this case a simulator running on the same computer)
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)

def arm_and_takeoff(target_altitude):
    """
    Arms vehicle and fly to a target_altitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print("Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    # after Vehicle.simple_takeoff will execute immediately).
    while True:
        print("Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def fly_circle(radius, altitude):
    """
    Fly the vehicle in a circular pattern.
    """

    print("Flying in a circular pattern...")
    # Get current location
    current_location = vehicle.location.global_relative_frame

    # Calculate waypoints for the circle
    num_waypoints = 36  # Adjust the number of waypoints for smoother circle
    for i in range(num_waypoints):
        angle = math.radians(float(i) / num_waypoints * 360)
        x = current_location.lon + (radius * math.cos(angle))
        y = current_location.lat + (radius * math.sin(angle))
        waypoint = LocationGlobalRelative(y, x, altitude)
        vehicle.simple_goto(waypoint)
        time.sleep(2)  # Adjust the delay between waypoints

def return_to_launch():
    """
    Return the vehicle to launch (RTL) mode.
    """

    print("Returning to launch...")
    vehicle.mode = VehicleMode("RTL")
    # Wait for the vehicle to switch to RTL mode
    while vehicle.mode.name != 'RTL':
        time.sleep(1)

# Set altitude for the circular flight pattern
target_altitude = 40
# Set radius of the circle
circle_radius = 0.008983  # 1 km equivalent in latitude/longitude

# Execute the mission
try:
    arm_and_takeoff(target_altitude)
    fly_circle(circle_radius, target_altitude)
    return_to_launch()
except KeyboardInterrupt:
    print("Mission interrupted by user.")
finally:
    # Close vehicle object before exiting script
    vehicle.close()
    print("Vehicle object closed.")

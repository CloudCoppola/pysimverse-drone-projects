"""
Drone Takeoff and Landing Demonstration using PySimVerse.

This script demonstrates how to safely command a drone to take off and
land within the PySimVerse simulation environment. It establishes a
connection to the simulator, initiates a controlled takeoff to a
specified height, and then performs a landing sequence.

The script is intended as a simple example of using high-level drone
control methods.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off to 100 cm.
5. Command the drone to land.
6. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to observe
the drone take off and land.

Note:
- The simulator must be running before execution.
- No explicit checks are performed to confirm successful connection,
  takeoff, or landing.
"""

import time
from pysimverse import Drone

drone = Drone() # Create a drone object 
drone.connect() # Connect to the drone

drone.take_off(takeoff_height=100)  # Drone take off 100 cm  

drone.land() # Land drone
time.sleep(5) # Wait 5 seconds 
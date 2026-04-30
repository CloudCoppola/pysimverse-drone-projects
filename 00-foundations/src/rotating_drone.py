"""
Drone Rotation Demonstration using PySimVerse.

This script demonstrates how to rotate a drone using degree-based
rotation commands within the PySimVerse simulation environment.
It establishes a connection to the simulator, performs a takeoff,
executes a rotation, and then lands the drone.

The example highlights the use of angular control through a
high-level rotation method.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off to 100 cm.
5. Rotate the drone by +180 degrees.
6. Command the drone to land.
7. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to observe
the drone taking off, rotating, and landing.

Note:
- The simulator must be running before execution.
- No validation is performed to confirm successful connection,
  rotation completion, or landing.
- The rotation command is issued without feedback or state checks,
  so the final orientation depends on the simulator's internal handling.
"""

import time
from pysimverse import Drone

drone = Drone() # Create drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=100)  # Take off 100 cm

drone.rotate(180)   # Rotate +180 degrees

drone.land()    # Land drone
time.sleep(5)   # Wait 5 seconds
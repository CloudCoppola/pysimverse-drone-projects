"""
Drone Forward Movement Demonstration using PySimVerse.

This script demonstrates how to command a drone to move forward by a
specified distance within the PySimVerse simulation environment. It
establishes a connection to the simulator, performs a takeoff to a
defined height, executes a forward movement, and then lands the drone.

The example highlights the use of simple, high-level motion commands.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off to 100 cm.
5. Move the drone forward by 100 cm.
6. Command the drone to land.
7. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to observe
the drone taking off, moving forward, and landing.

Note:
- The simulator must be running before execution.
- No validation is performed to confirm successful connection,
  movement execution, or landing.
- Movement commands are issued sequentially without feedback or
  state checks, so actual behaviour depends on the simulator's
  internal handling of these commands.
"""

import time
from pysimverse import Drone

drone = Drone() # Create drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=100)  # Drone take off 100 cm

drone.move_forward(100) # Move drone forwards by 100 cm 

drone.land()    # Land drone
time.sleep(5)   # Wait 5 seconds
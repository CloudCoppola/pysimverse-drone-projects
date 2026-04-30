"""
Drone Multi-Directional Movement Demonstration using PySimVerse.

This script demonstrates how to control a drone using multiple
directional movement commands within the PySimVerse simulation
environment. It connects to the simulator, performs a takeoff,
executes a sequence of movements (forward, left, right, and backward),
and then lands the drone.

The example illustrates the use of high-level motion commands to
navigate the drone in different directions.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off to 100 cm.
5. Execute directional movements:
   - Move forward by 100 cm
   - Move left by 100 cm
   - Move right by 100 cm
   - Move backward by 100 cm
6. Command the drone to land.
7. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to observe
the drone performing a sequence of directional movements.

Note:
- The simulator must be running before execution.
- Movement commands are issued sequentially without confirmation of
  completion, so behaviour depends on the simulator's internal handling.
- No validation is performed to confirm successful connection,
  motion execution, or landing.
"""

import time
from pysimverse import Drone

drone = Drone() # Create a drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=100)  # Take off 100 cm

drone.move_forward(100) # Move forwards 100 cm
drone.move_left(100)    # Move left 100 cm
drone.move_right(100)   # Move right 100 cm
drone.move_backward(100)    # Move backwards 100 cm

drone.land() # Land drone
time.sleep(5) # Wait 5 seconds
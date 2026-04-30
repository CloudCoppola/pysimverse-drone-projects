"""
Garage Mission Demonstration (Level 1) using PySimVerse.

This script demonstrates a simple sequence of drone commands intended
to approximate completion of the Garage mission within the PySimVerse
simulation environment. The drone takes off, moves toward a target
location using fixed distance commands, and lands.

The example highlights how movement distances and speed settings
influence the drone's trajectory and execution timing.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off.
5. Set linear movement speeds.
6. Move the drone forward.
7. Move the drone right. 
8. Command the drone to land.
9. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to observe
the drone executing a predefined path toward the target area.

Note:
- The simulator must be running before execution.
- The trajectory is open-loop and based on fixed distance commands;
  no feedback is used to correct position or ensure accurate landing.
- No validation is performed to confirm mission success, timing,
  or final alignment with the target.
- Completion speed and "star" outcomes are not measured or optimised
  within this script.
"""

import time
from pysimverse import Drone

drone = Drone() # Create drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=100)  # Take off 

drone.set_speed(50) # Set speed to 50 sec/s

drone.move_forward(250) # Move forwards

drone.move_right(255)   # Move right

drone.land()    # Land drone
time.sleep(5)   # Wait 5 seconds
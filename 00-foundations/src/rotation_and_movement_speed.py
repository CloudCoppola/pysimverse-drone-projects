"""
Drone Speed and Rotation Control Demonstration using PySimVerse.

This script demonstrates how to control both linear movement speed and
rotational speed of a drone within the PySimVerse simulation environment.
It connects to the simulator, performs a takeoff, adjusts movement and
rotation speeds, executes motion commands, and then lands the drone.

The example highlights how speed parameters influence drone behaviour
when executing movement and rotation commands.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off to 100 cm.
5. Set linear movement speed to 50 cm/s.
6. Move the drone forward by 100 cm.
7. Set rotation speed to 90 degrees per second.
8. Rotate the drone by 180 degrees.
9. Command the drone to land.
10. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to observe
how different speed settings affect forward movement and rotation.

Note:
- The simulator must be running before execution.
- Speed settings are applied prior to issuing movement and rotation
  commands, but no validation is performed to confirm their effect.
- Commands are executed sequentially without feedback or state checks,
  so actual motion and timing depend on the simulator's internal handling.
"""

import time
from pysimverse import Drone

drone = Drone() # Create a drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=100)  # Take off 100 cm

drone.set_speed(50) # Set movement speed to 50 cm/s
drone.move_forward(100) # Move forwards 100 cm

drone.set_rotation_speed(90)    # Set rotation speed to 90 deg/s
drone.rotate(180)   # Rotate 180 degrees 

drone.land()    # Land drone
time.sleep(5)   # Wait 5 seconds 
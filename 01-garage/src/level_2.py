"""
Multi-Target Navigation Demonstration (Level 2) using PySimVerse.

This script demonstrates a predefined sequence of drone movements
intended to visit multiple target locations in order within the
PySimVerse simulation environment. The drone takes off, executes a
series of rotations and forward movements to approximate target
positions, and then lands.

The example highlights how combining rotation and translation
commands can be used to construct a simple navigation path.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off.
5. Set linear movement speed.
6. Navigate through a sequence of targets:
   - Target 1: rotate left and move forward
   - Target 2: rotate right and move forward
   - Target 3: rotate slightly and move forward
7. Command the drone to land.
8. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to observe
the drone following a predefined multi-step trajectory.

Note:
- The simulator must be running before execution.
- Target positions are approximated using fixed rotations and distances;
  no feedback or sensing is used to confirm arrival at each target.
- Rotations and movements are issued sequentially without validation
  of completion or accuracy.
- Final task completion is not explicitly verified.
"""

import time
from pysimverse import Drone

drone = Drone() # Create drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=100)  # Take off 

drone.set_speed(50) # Set speed 

# Target 1
drone.rotate(-80)   # Rotate left 
drone.move_forward(240) # Move forwards

# Target 2
drone.rotate(140)   # Rotate right
drone.move_forward(260) # Move forwards

# Target 3
drone.rotate(10)    # Rotate right 
drone.move_forward(300) # Move forwards

drone.land() # Land drone
time.sleep(5)   # Wait 5 seconds
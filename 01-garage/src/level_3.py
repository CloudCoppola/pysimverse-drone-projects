"""
Multi-Target Fly-Through and Landing Demonstration (Level 3) using PySimVerse.

This script demonstrates a predefined sequence of drone movements
intended to pass through intermediate target regions and land at a
final location within the PySimVerse simulation environment. The drone
takes off, executes a series of rotations and forward movements, and
then performs a landing.

The example illustrates how longer-distance movements combined with
rotational adjustments can approximate a multi-stage trajectory.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off to 50 cm.
5. Set linear movement speed.
6. Execute a sequence of movements:
   - Target 1: rotate left and move forward
   - Target 2: rotate right and move forward
7. Command the drone to land.
8. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to observe
the drone following a predefined trajectory through intermediate
regions and landing.

Note:
- The simulator must be running before execution.
- The trajectory is defined using fixed rotations and distances;
  no sensing or feedback is used to confirm passing through targets.
- Movements are executed sequentially without validation of completion
  or positional accuracy.
- Landing location is not verified against a target region.
"""

import time 
from pysimverse import Drone

drone = Drone() # Create drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=50)   # Take off

drone.set_speed(50) # Set speed

# Target 1
drone.rotate(-35)   # Rotate left
drone.move_forward(400) # Move forwards

# Target 2
drone.rotate(150)   # Rotate right
drone.move_forward(550) # Move forwards


drone.land()    # Land drone
time.sleep(5)   # Wait 5 seconds
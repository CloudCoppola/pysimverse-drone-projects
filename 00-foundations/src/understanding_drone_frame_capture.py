"""
Drone Camera Frame Retrieval Demonstration using PySimVerse.

This script demonstrates how to retrieve a camera frame from the drone
using the get_frame() method within the PySimVerse simulation environment.
It connects to the simulator, performs a takeoff, requests a single frame
from the drone's camera, and then lands the drone.

The example highlights how to access visual data that can be used for
display, processing, or recording in more advanced applications.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off to 100 cm.
5. Retrieve a camera frame using get_frame().
6. Command the drone to land.
7. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to retrieve
a camera frame from the drone.

Note:
- The simulator must be running before execution.
- The retrieved frame is not stored, displayed, or processed in this script.
- No validation is performed to confirm successful connection,
  frame retrieval, or landing.
- This example retrieves a single frame rather than a continuous stream.
"""

import time
from pysimverse import Drone

drone = Drone() # Create drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=100)  # Take off 100 cm 

drone.get_frame()   # Get camera frame from drone

drone.land()   # Land drone    
time.sleep(5)  # Wait 5 seconds
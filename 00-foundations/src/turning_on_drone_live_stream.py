"""
Drone Camera Stream Activation using PySimVerse.

This script demonstrates how to enable the drone's live camera stream
within the PySimVerse simulation environment. It establishes a connection
to the simulator, performs a takeoff, activates the video stream, and
then lands the drone.

The example highlights the use of the stream-on method to access the
drone's onboard camera feed.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Command the drone to take off to 100 cm.
5. Enable the drone's camera stream.
6. Command the drone to land.
7. Pause execution briefly.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run this script while the PySimVerse simulator is active to enable
the drone's live camera stream.

Note:
- The simulator must be running before execution.
- Enabling the stream does not display or process the video feed;
  additional code is required to retrieve and visualise frames.
- No validation is performed to confirm successful connection,
  stream activation, or landing.
"""

import time
from pysimverse import Drone

drone = Drone() # Create drone object
drone.connect() # Connect to drone

drone.take_off(takeoff_height=100)  # Take off 100 cm

drone.streamon() # Turn stream on

drone.land()    # Land drone 
time.sleep(5)   # Wait 5 seconds
"""
Connect to a Drone in PySimVerse Simulation Environment.

This script demonstrates how to establish a connection between a Python
environment (e.g., PyCharm) and a drone simulator using the PySimVerse API.
It creates a drone instance, initiates a connection to the simulator, and
pauses execution briefly to allow the connection to stabilise.

The successful connection can be verified through console output and
the simulator interface.

Steps performed:
1. Import required libraries.
2. Create a Drone object.
3. Connect to the drone simulator.
4. Wait for a short duration to confirm the connection.

Dependencies:
- pysimverse
- time (standard library)

Usage:
Run the script while the PySimVerse simulator is active to establish
and verify the connection.

Note:
Ensure the simulator is running before executing this script,
otherwise the connection attempt may fail.
"""

import time
from pysimverse import Drone

drone = Drone() # Create a drone object 

drone.connect() # Connect to the drone 

time.sleep(5)   # Wait for 5 seconds
# 00-foundations

This module introduces the fundamental concepts of controlling a drone in the PySimVerse simulation environment. Each script demonstrates a specific capability, progressing from basic connection to movement, rotation, and basic perception.

These examples focus on **API usage and command execution**, not full control validation or closed-loop autonomy.

## Scripts Overview

This module contains a set of foundational scripts that demonstrate core drone control capabilities using PySimVerse. Each script focuses on a specific concept, progressing from basic connection to movement, rotation, and camera interaction.

| Script Name                                  | Description                                                                 |
|---------------------------------------------|-----------------------------------------------------------------------------|
| `drone_connection.py`                        | Establishes a connection between the Python environment and the simulator. |
| `first_flight.py`                            | Demonstrates basic takeoff and landing.                                     |
| `moving_drone_forward.py`                    | Moves the drone forward by a specified distance.                            |
| `drone_movements.py`                         | Executes multiple directional movements (forward, left, right, backward).   |
| `rotating_drone.py`                          | Rotates the drone using degree-based commands.                              |
| `rotation_and_movement_speed.py`             | Controls linear and rotational speed during movement and rotation.          |
| `turning_on_drone_live_stream.py`            | Enables the drone’s live camera stream.                                     |
| `understanding_drone_frame_capture.py`       | Retrieves a camera frame from the drone.                                    |

---

### Notes

- These scripts demonstrate **how to use the API**, not how to build robust control systems.
- Commands are issued without validation or feedback.
- Camera-related scripts enable access to data but do not include processing or visualisation.

---
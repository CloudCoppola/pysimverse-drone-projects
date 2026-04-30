# 01-garage

This module introduces simple mission-based drone navigation tasks in the PySimVerse simulation environment. The focus is on executing predefined movement sequences to approximate task completion in a structured environment.

The Garage missions extend the foundational concepts by combining movement, rotation, and speed control to reach target areas.

## Objectives

- Navigate the drone toward one or more target locations
- Combine rotation and translation commands
- Understand how distance and speed affect trajectory
- Execute multi-step movement sequences
- Approximate landing at a target location

## Scripts Overview

| Script Name   | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `level_1.py` | Moves the drone toward a target location and performs a landing sequence.   |
| `level_2.py` | Executes a sequence of movements to visit multiple target locations.        |
| `level_3.py` | Follows a longer trajectory passing through intermediate targets and lands. |

## Key Concepts

### 1. Open-Loop Navigation
All missions are executed using predefined commands:
- Fixed distances (e.g., `move_forward(250)`)
- Fixed rotations (e.g., `rotate(-80)`)

There is **no feedback mechanism** to:
- Confirm position
- Correct trajectory
- Validate target arrival

### 2. Command Sequencing
Navigation is achieved by chaining commands:
- Rotate -> Move -> Rotate -> Move

This creates a piecewise trajectory rather than a continuous path.

### 3. Speed Control
Movement speed influences:
- Execution time
- Motion smoothness (simulator-dependent)
- Task completion duration (e.g., faster completion → more stars in the simulator)

### 4. Approximate Targeting
Targets are not explicitly represented in code.
Instead:
- Movements are manually tuned to *approximate* target positions
- Success depends on consistent initial conditions

## How to Run

Ensure the PySimVerse simulator is running, then execute a script:

```bash
python level_1.py
```
# Mouse Restrictor - README

## Description

**Mouse Restrictor** is a Python application designed to restrict the movement of the mouse cursor within a defined area on the screen. It features a graphical user interface for debugging and provides key bindings for easy control. The application continuously monitors mouse inactivity and recenters the cursor if it hasn't moved for a specified duration. It is intended to simulate the behavior of a joystick by controlling the pointer in the Windows API.

## Features

- **Activate/Deactivate Cursor Restriction**: Toggle the mouse restriction on and off using a global keyboard shortcut.
- **Debug Window**: View real-time debugging information in a separate window.
- **Mouse Inactivity Monitoring**: Automatically recenter the cursor after a period of inactivity.
- **Global Keyboard Shortcuts**:
  - `F1`: Activate/Deactivate cursor restriction.
  - `F2`: Open the debug window.
  - `F4`: Exit the application.

## Requirements

- Python 3.x
- The following Python libraries:
  - `ctypes`
  - `time`
  - `threading`
  - `keyboard`
  - `tkinter`

## Installation

1. **Install Python**: Ensure that Python 3.x is installed on your system.
2. **Install Required Libraries**:
   - Install the `keyboard` library using pip:
     ```
     pip install keyboard
     ```
   - `ctypes` and `tkinter` are part of the standard Python library and do not need to be installed separately.

## Usage

1. **Run the Application**:
   - Save the provided Python script to a file, e.g., `mouse_restrictor.py`.
   - Execute the script:
     ```
     python mouse_restrictor.py
     ```

2. **Control the Application**:
   - **F1**: Press `F1` to toggle the mouse restriction on and off. When activated, the cursor will be confined to a 200x200 pixel area at the center of the screen.
   - **F2**: Press `F2` to open the debug window, which provides real-time information about the application's status, including whether the restriction is active, the time elapsed since the last mouse movement, and the number of times the cursor has been recentered.
   - **F4**: Press `F4` to quit the application.

## Detailed Functionality

- **Mouse Restriction**:
  - When activated, the cursor is confined to a 200x200 pixel area at the center of the screen.
  - The restricted area is defined using `ctypes` to interact with the Windows API.

- **Mouse Inactivity Monitoring**:
  - The application monitors the mouse position and recenters the cursor if it remains inactive for more than 0.25 seconds.

- **Debug Window**:
  - The debug window provides a text area for logging messages and a label displaying real-time information about the application's status.

## Code Overview

- **Main Class**: `MouseRestrictor`
  - **Initialization**: Sets up the application, keyboard shortcuts, and initializes Tkinter.
  - **toggle_restriction()**: Toggles the restriction on and off.
  - **activate()**: Activates the mouse restriction.
  - **deactivate()**: Deactivates the mouse restriction.
  - **update_clip()**: Sets the restricted area.
  - **release_clip()**: Releases the mouse from the restricted area.
  - **print_message()**: Logs messages to the debug window.
  - **open_debug_window()**: Opens the debug window.
  - **show_debug_window()**: Displays the debug window.
  - **update_debug_info()**: Updates the debug window with real-time information.
  - **on_debug_window_close()**: Handles the debug window close event.
  - **stop()**: Stops the application.
  - **center_cursor()**: Recenters the mouse cursor.
  - **monitor_mouse_inactivity()**: Monitors mouse inactivity and recenters the cursor if necessary.

## Notes

- This application is intended for use on Windows operating systems due to the reliance on the Windows API via `ctypes`.
- Ensure that the `keyboard` library is installed with sufficient permissions to capture global key presses.

Enjoy using the Mouse Restrictor to control your mouse cursor movement!

# xPantherRDP

This script automates mouse clicks at a specified location when the "Microsoft Remote Desktop" application is running. The script checks if the application is running every 5 minutes (300 seconds) and performs a mouse click at the coordinates (100, 100) if the application is active.

![files](./Images/xpanther.png)

## Prerequisites

- macOS or Windows
- Python 3.10

## Dependencies

For macOS:
- Quartz (part of the `pyobjc` framework)

For Windows:
- `pyautogui`
- `psutil`

## Installation

1. **Install Python 3.10**

2. **Install Dependencies**:
   
   For macOS:
   ```bash
   pip install pyobjc
   ```

   For Windows:
   ```bash
   pip install pyautogui psutil
    ```

## Script Overview

**Platform Detection:** The script detects the operating system using `platform.system()`.

**Function Definitions:**

For macOS:
* `is_application_running(app_name)`: Checks if the specified application is running using the `pgrep` command.
* `click(x, y)`: Uses Quartz to simulate a mouse click at the specified coordinates.

For Windows:
* `is_application_running(app_name)`: Checks if the specified application is running using `psutil`.
* `click(x, y)`: Uses `pyautogui` to simulate a mouse click at the specified coordinates.

**Main Loop:** Continuously checks if the "Microsoft Remote Desktop" application is running every 5 minutes. If it is running, it performs a click at the specified coordinates and prints a message to the console.

## Customization

**Adjust the Sleep Interval:** The sleep interval can be changed by modifying the `time.sleep(300)` line. The current setting waits for 5 minutes (300 seconds) between checks.

**Change Click Coordinates:** Modify the `(100, 100)` coordinates in the `click` function to change where the click occurs.

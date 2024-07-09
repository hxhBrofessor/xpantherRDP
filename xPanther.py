import platform
import time

# Check if the script is running on a macOS system
if platform.system() == "Darwin":  # macOS
    import Quartz
    import subprocess


    # Function checks if an app is running on macOS system by using subprocess to execute the "pgrep" command
    def is_application_running(app_name):
        process = subprocess.Popen(["pgrep", app_name], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        return bool(output.strip())


    # Simulates a mouse click on a macOS system at coordinates x and y
    def click(x, y):
        # Get the current mouse position
        current_pos = Quartz.CGEventGetLocation(Quartz.CGEventCreate(None))
        current_x, current_y = current_pos.x, current_pos.y

        # Move mouse cursor to the desired position, simulate a click, and move cursor back to original position
        move = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventMouseMoved, (x, y), Quartz.kCGMouseButtonLeft)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, move)
        click_down = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDown, (x, y),
                                                    Quartz.kCGMouseButtonLeft)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, click_down)
        click_up = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseUp, (x, y), Quartz.kCGMouseButtonLeft)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, click_up)
        move_back = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventMouseMoved, (current_x, current_y),
                                                   Quartz.kCGMouseButtonLeft)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, move_back)

# Check if the script is running on a Windows system
elif platform.system() == "Windows":
    import pyautogui
    import psutil


    # Function checks if an app is running on Windows system by iterating over all running processes
    def is_application_running(app_name):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == app_name:
                return True
        return False


    # Simulates a mouse click on a Windows system at coordinates x and y
    def click(x, y):
        # Get the current mouse position
        current_x, current_y = pyautogui.position()

        # Move mouse cursor to the desired position and click, then move cursor back to original position
        pyautogui.click(x, y)
        pyautogui.moveTo(current_x, current_y)

# If the script is running on neither macOS nor Windows, raise an error
else:
    raise EnvironmentError("Unsupported operating system")

# Entry point for the script's execution
if __name__ == "__main__":
    while True:
        # Use the appropriate application name for the system's platform and check if it's running
        app_name = "Microsoft Remote Desktop" if platform.system() == "Darwin" else "mstsc.exe"
        if is_application_running(app_name):
            # If the application is running, simulate a click at the specified coordinates (adjust as necessary)
            click(100, 100)
        # Wait for 5 minutes before repeating the loop
        time.sleep(300)
        # Print a message to show that a click was performed
        print("RDP session clicked")

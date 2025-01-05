import os
import time
import keyboard  # Importing the keyboard library

# Welcome message and instructions
print("Welcome to the System Control Program!")
print("\nInstructions:")
print("Press 'S' to Shutdown")
print("Press 'R' to Restart")
print("Press 'L' to Sleep")
print("Press 'E' to Exit\n")
print("Waiting for your input...")

# Main loop
while True:
    # Detect key presses for specific actions
    if keyboard.is_pressed('s'):  # Shutdown
        print("\nYou pressed 'S' to shutdown the system.")
        time.sleep(1)  # Small delay for user confirmation
        print("Shutting down in 3 seconds...")
        time.sleep(3)
        os.system("shutdown /s /t 1")
        break

    elif keyboard.is_pressed('r'):  # Restart
        print("\nYou pressed 'R' to restart the system.")
        time.sleep(1)
        print("Restarting in 3 seconds...")
        time.sleep(3)
        os.system("shutdown /r /t 1")
        break

    elif keyboard.is_pressed('l'):  # Sleep
        print("\nYou pressed 'L' to put the system to sleep.")
        time.sleep(1)
        print("Going to sleep in 3 seconds...")
        time.sleep(3)
        # Use the powercfg command to put the system to sleep
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        break

    elif keyboard.is_pressed('e'):  # Exit
        print("\nYou pressed 'E' to exit the program.")
        time.sleep(1)
        print("Exiting the program. Goodbye!")
        break
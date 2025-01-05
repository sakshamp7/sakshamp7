#This code is use when user does not wants to use keyboard function for brightness
# import screen_brightness_control as screen         
# screen.set_brightness(50)
# get=screen.get_brightness()
# print(get)

import screen_brightness_control as screen    #This code is use when user wants to use keyboard function for brightness
import keyboard

def increase_brightness():
    try:
        current_brightness = screen.get_brightness()  # This returns a list
        # Get the brightness of the first display (or handle multiple displays as needed)
        new_brightness = min(current_brightness[0] + 10, 100)  # Increase by 10, max 100%
        screen.set_brightness(new_brightness)
        print(f"Brightness increased to {new_brightness}%")
    except Exception as e:
        print(f"Error increasing brightness: {e}")

def decrease_brightness():
    try:
        current_brightness = screen.get_brightness()  # This returns a list
        # Get the brightness of the first display (or handle multiple displays as needed)
        new_brightness = max(current_brightness[0] - 10, 0)  # Decrease by 10, min 0%
        screen.set_brightness(new_brightness)
        print(f"Brightness decreased to {new_brightness}%")
    except Exception as e:
        print(f"Error decreasing brightness: {e}")

# Set up keyboard listeners
keyboard.add_hotkey('ctrl+B', increase_brightness)   # Increase brightness with Ctrl + Up Arrow
keyboard.add_hotkey('ctrl+D', decrease_brightness)  # Decrease brightness with Ctrl + Down Arrow

print("Press Ctrl + B to increase brightness and Ctrl + D to decrease brightness.")
print("Press Esc to exit.")

# Keep the program running
keyboard.wait('esc')  # Exit the program when Esc is pressed 
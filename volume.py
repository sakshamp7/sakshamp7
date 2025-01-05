from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import keyboard
import time

# Get the audio endpoint volume interface
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Initialize step sizes
increase_step = 2
decrease_step = 2

# Function to adjust volume
def change_volume(delta):
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(0.0, min(1.0, current_volume + delta / 100))
    volume.SetMasterVolumeLevelScalar(new_volume, None)

# Function to display the current volume percentage
def get_volume_percentage():
    return int(volume.GetMasterVolumeLevelScalar() * 100)

# Main loop
print("Press '+' to increase volume, '-' to decrease volume, and 'Esc' to exit.")

while True:
    if keyboard.is_pressed('+'):  # Increase volume
        change_volume(increase_step)
        print(f"Volume: {get_volume_percentage()}%")
        increase_step += 2  # Increment step size
        decrease_step = 2  # Reset opposite step size
        time.sleep(0.3)  # Add delay to prevent rapid changes
    elif keyboard.is_pressed('-'):  # Decrease volume
        change_volume(-decrease_step)
        print(f"Volume: {get_volume_percentage()}%")
        decrease_step += 2  # Increment step size
        increase_step = 2  # Reset opposite step size
        time.sleep(0.3)  # Add delay to prevent rapid changes
    elif keyboard.is_pressed('esc'):  # Exit
        print("Exiting...")
        break

# Import necessary libraries
from cv2 import imread
from gui_automation import GuiAuto
import pyautogui

# Set the pause duration for pyautogui actions
pyautogui.PAUSE = 0.1

# Get the number of times to refresh from user input
timeRefresh = int(input("How many times do you want to refresh: "))

# Loop through the specified number of refreshes
for i in range(timeRefresh):
    
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Calculate the coordinates for the right-click action
    x = screen_width/2
    y = screen_height/2

    # Perform a right-click at the specified coordinates
    pyautogui.rightClick(x, y)

    # Initialize GuiAuto for GUI automation
    Gcurser = GuiAuto()

    # Detect a specific image ('sonref.png') on the screen and click it if found
    if Gcurser.detect(imread('.\icon\Refresh.png'), 0.8):
        Gcurser.click()

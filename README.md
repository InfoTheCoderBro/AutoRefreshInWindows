# AutoRefreshInWindows
This Python script is designed for automating Refresh process in windows. It leverages several libraries to achieve this automation:

1. cv2 is used to read image files.
2. gui_automation is a custom library, presumably for GUI automation tasks.
3. pyautogui is used for controlling the mouse.

The script follows these steps:

1. It sets the pause duration for PyAutoGUI actions to 0.1 seconds to ensure smooth automation.

2. It prompts the user to input the number of times they want to refresh something. This value is stored in the timeRefresh variable.

3. The script then enters a loop, repeating the specified number of refreshes.

4. Inside the loop, it retrieves the screen dimensions and calculates the coordinates for a right-click action at the center of the screen.

5. A right-click action is performed at the calculated coordinates using PyAutoGUI.

6. It initializes the GuiAuto class, presumably for further GUI automation.

7. The script attempts to detect a specific image named 'Refresh.png' on the screen using OpenCV (cv2). If the image is found with a confidence level of at least 80% (0.8), it clicks on it using the GuiAuto instance.








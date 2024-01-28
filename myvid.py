# Point 1: Install necessary packages



import subprocess
import sys

def install_pip():
    try:
        subprocess.run([sys.executable, '-m', 'ensurepip', '--default-pip'], check=True)
        print("pip installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during pip installation: {e}")
        exit()

# Check if pip is installed
try:
    subprocess.run(['pip', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print("pip is already installed.")
except subprocess.CalledProcessError:
    print("pip is not installed. Installing now...")
    install_pip()




try:
    subprocess.run(['pip', 'install', 'opencv-python', 'numpy'])
except Exception as e:
    print(f"An error occurred during package installation: {e}")
    # exit()

import cv2
import numpy as np
import platform
import os
import datetime


# Prompt:
"""
1. Create a Python script that installs the necessary packages for video generation. 
   Use 'pip install opencv-python numpy' to install OpenCV and NumPy.

2. Develop a script using the installed packages to generate a 720p video. 
   The video should showcase six bouncing balls of different colors, each moving independently and interacting with the frame's edges. 
   Include sleek text at the bottom of each frame, indicating that the video was made with ChatGPT. 
   Provide detailed text output during the video generation process, including frame numbers, positions of each ball, 
   and information about the program and video creation (e.g., timestamps, credits, acknowledgments). 
   The video should consist of 600 frames.

3. Add a script command at the end of the program that automatically opens the generated video file. 
   Provide clear instructions for viewing the video using the default video player on different operating systems 
   (Linux, macOS, and Windows).
"""



# Point 2: Create a 720p video with bouncing balls and sleek text
width, height = 1280, 720
output_file = 'output_video_720p_6_balls_text.avi'
video_writer = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))

balls = [
    {"x": 50, "y": 50, "velocity_x": 5, "velocity_y": 3, "color": (0, 0, 255)},  # Red ball
    {"x": 200, "y": 150, "velocity_x": 3, "velocity_y": 2, "color": (255, 0, 0)},  # Blue ball
    {"x": 400, "y": 100, "velocity_x": -4, "velocity_y": -2, "color": (0, 255, 0)},  # Green ball
    {"x": 600, "y": 200, "velocity_x": -2, "velocity_y": 4, "color": (255, 255, 0)},  # Yellow ball
    {"x": 800, "y": 300, "velocity_x": 3, "velocity_y": -3, "color": (0, 255, 255)},  # Cyan ball
    {"x": 1000, "y": 400, "velocity_x": -3, "velocity_y": 3, "color": (255, 0, 255)}  # Magenta ball
]

gravity = 0.2
num_frames = 600  # Updated to 600 frames

program_creation_datetime = datetime.datetime.now()
video_creation_datetime = None

for frame in range(num_frames):
    img = 255 * np.ones((height, width, 3), dtype=np.uint8)

    for ball in balls:
        cv2.circle(img, (int(ball["x"]), int(ball["y"])), 20, ball["color"], -1)

    cv2.putText(img, "Video made with ChatGPT", (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    for ball in balls:
        ball["x"] += ball["velocity_x"]
        ball["y"] += ball["velocity_y"]
        ball["velocity_y"] += gravity

        if ball["x"] - 20 <= 0 or ball["x"] + 20 >= width:
            ball["velocity_x"] *= -1

        if ball["y"] + 20 >= height:
            ball["y"] = height - 20
            ball["velocity_y"] *= -0.8

    video_writer.write(img)

    print(f'Frame: {frame + 1}/{num_frames}, Ball Positions: {[(ball["x"], ball["y"]) for ball in balls]}')

    if frame == 0:
        video_creation_datetime = datetime.datetime.now()

video_writer.release()

full_path = os.path.abspath(output_file)

print(f'\nVideo generation complete. Check the output file at:\n{full_path}\n')
print(f'Program created on: {program_creation_datetime}')
print(f'Video created on: {video_creation_datetime}')
print('Credits:')
print(f'  - Python {platform.python_version()}')
print('  - OpenCV (https://opencv.org/)')
print('  - NumPy (https://numpy.org/)')
print('\nThanks to the developers and contributors of the above libraries and models!')

# Point 3: Play the video automatically using the default video player
try:
    subprocess.run(['xdg-open', output_file])  # For Linux
except Exception:
    try:
        subprocess.run(['open', output_file])  # For macOS
    except Exception:
        os.system(output_file)  # For Windows or if the above commands fail

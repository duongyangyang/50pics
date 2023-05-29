import cv2
import os
import numpy as np

directory = os.getcwd() # getting the current directory
name_video = "Duongduong.mp4" # entering the name of the file to be read
## Step 1
# Creating a directory for the video frames named original_frames
 
try:
	if not os.path.exists('original_frames'): os.makedirs('original_frames')
except OSError:
	print("It was not possible to create the 'original_frames' directory")
 
#creating a video instance
cap = cv2.VideoCapture(0)
 
# checking some video properties
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
 
# Initializing an auxiliary variable to extract each frame from the video
current_frame = 0
 
# Transforming each frame of the video into a .jpg image
 
while (True):
	ret, frame = cap.read()
 
	if ret == True and current_frame < 201:
		name = './original_frames/frame' + str(current_frame) + '.jpg'
		print("Criating... " + name)
 
		cv2.imwrite(name,frame) # saving the image at the frame "current_frame"
 
		current_frame += 1 # next frame
	else:
		break
 
cap.release() # releasing the video
cv2.destroyAllWindows() # destroying the windows
print("Done!")

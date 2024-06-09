#### Housekeeping
# Libraries
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep


#### Code that makes my original image on the LED matrix
# Declare my colors as RGB values and store them in variables
d = (255, 255, 255) # Cyan
f = (25, 25, 112) # MidnightBlue
g = (0, 191, 255) # DeepSkyBlue
b = (0, 0, 0) # Black

# Arrange my colors on an 8x8 matrix to make an image. This is a whale I made.
image = [
  f, f, f, g, g, g, g, g,
  f, f, g, g, f, g, g, f,
  f, f, f, f, f, f, g, g,
  f, g, g, g, g, g, g, g,
  g, g, g, g, g, g, d, d,
  g, b, g, g, g, d, d, f,
  g, g, g, g, d, d, f, f,
  f, g, g, d, d, f, f, f]
 
# Code telling the pixels to light up
sense.set_pixels(image)

sleep(1) # numbers are in seconds

'''
#### Code for using the color sensor
# Set up the sensors
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Use the sensor
rgb = sense.color # get the colour from the sensor
f = (rgb.red, rgb.green, rgb.blue) # re-assign the variable "f" to be the sensed color

# Arrange my colors on an 8x8 matrix.
image = [
  f, f, f, g, g, g, g, g,
  f, f, g, g, f, g, g, f,
  f, f, f, f, f, g, g, f,
  f, g, g, g, g, g, g, f,
  g, g, g, g, g, g, d, f,
  g, b, g, g, g, d, d, f,
  g, g, g, g, d, d, f, f,
  f, g, g, d, d, f, f, f]
  
  
# Code telling the pixels to light up
sense.set_pixels(image)

sleep(1)


#### Create the GIF
# Make a For Loop to run for the seconds left over 
for i in range(28):
  rgb = sense.color # get the color from the sensor
  f = (rgb.red, rgb.green, rgb.blue)
  
  # Arrange my colors on an 8x8 matrix
  image = [
    f, f, f, g, g, g, g, g,
    f, f, g, g, f, g, g, f,
    f, f, f, f, f, g, g, f,
    f, g, g, g, g, g, g, f,
    g, g, g, g, g, g, d, f,
    g, b, g, g, g, d, d, f,
    g, g, g, g, d, d, f, f,
    f, g, g, d, d, f, f, f]
  
  # Code telling the pixels to light up
  sense.set_pixels(image)
  
  sleep(1) 

  
#### Rotate our creature  
while True:
	sense.set_rotation(0)
	sleep(1)
	sense.set_rotation(90)  
	sleep(1)  
	sense.flip_h()
	sleep(1)
	sense.set_rotation(0)
	sleep(1)
	sense.set_rotation(270)
	sleep(1)
	sense.flip_h()
	sleep(1)
	
'''
# Rotation sensors
orientation = sense.get_orientation_degrees()
roll = orientation["roll"]
pitch = orientation["pitch"]
yaw = orientation["yaw"]
if pitch > 180:
	pitch = pitch - 360

# Starting values
starting_position = roll * 0.1 + pitch * 0.6 + yaw * 0.3
movement = starting_position
direction = "starboard"

while True:
	# Poll the sensors at the start of the loop
	orientation = sense.get_orientation_degrees()
	roll = orientation["roll"]
	pitch = orientation["pitch"]
	yaw = orientation["yaw"]
	if pitch > 180:
		pitch = pitch - 360
		
	# Get a fresh orientation reading for this lap	
	new_movement = roll * 0.1 + pitch * 0.6 + yaw * 0.3
	
	# No direction change or movement if sensor difference is too small
	if abs(movement-new_movement) < 1:
		continue
	
	# Change creature direction to port
	if new_movement < movement and direction == "starboard":
		sense.flip_h()
		direction = "port"
	
	# Change creature direction to starboard
	if new_movement > movement and direction == "port":
		sense.flip_h()
		direction = "starboard"
	
	# Compare current orientation to our pre-loop starting orientation
	relative_heel = starting_position - new_movement
	
	# Rotate our creature
	if relative_heel > 3:
		sense.set_rotation(270)
		
	if relative_heel < -3:
		sense.set_rotation(90)
		
	if -3 <= relative_heel <= 3:
		print("Center!")
		sense.set_rotation(0)
	
	# Store this lap's movement value for comparison on the next iteration of the loop 
	movement = new_movement
	
	# Merely for observing our sensor data for debugging
	print(movement)
	

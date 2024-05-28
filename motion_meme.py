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
  f, f, f, f, f, g, g, f,
  f, g, g, g, g, g, g, f,
  g, g, g, g, g, g, d, f,
  g, b, g, g, g, d, d, f,
  g, g, g, g, d, d, f, f,
  f, g, g, d, d, f, f, f]
 
# Code telling the pixels to light up
sense.set_pixels(image)

sleep(1) # numbers are in seconds


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

previous_colors = f

sleep(1)


#### Create the GIF
# Make a For Loop to run for the seconds left over 
multiple = 0
for i in range(28):
  # Get orientation data
  orientation = sense.get_orientation_degrees()
  print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
  print(orientation["pitch"])
  
  pitch = orientation["pitch"]
  
  if pitch > 10:
    rotation_angle = 90
    print("right")
    
  elif pitch > 350:
    rotation_angle = 270
    print("left")
    
  else:
    rotation_angle = 0
    print("center")
  
  # Rotate the image
  '''
  rotation_angle = multiple * 90
  multiple = multiple + 1
  if multiple > 3:
    multiple = 0
  '''
  
  sense.set_rotation(rotation_angle)
  
  rgb = sense.color # get the colour from the sensor
  
  # Excentuate the increases and decreases in RGB values
  current_colors = (rgb.red, rgb.green, rgb.blue) # store the current sensed values for comparison with the previous colors
  changes = [current_colors[0]-previous_colors[0], current_colors[1]-previous_colors[1],current_colors[1]-previous_colors[1]]
  increase = min(changes)
  decrease = max(changes)
  increase_position = changes.index(increase)
  decrease_position = changes.index(decrease)
  
  modifier = 40
  
  current_colors_modified = list(current_colors)
  current_colors_modified[increase_position] = current_colors_modified[increase_position] + modifier
  current_colors_modified[decrease_position] = current_colors_modified[decrease_position] - modifier

  f = tuple(current_colors_modified)
  
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
  
  previous_colors = current_colors
  
  sleep(1) 

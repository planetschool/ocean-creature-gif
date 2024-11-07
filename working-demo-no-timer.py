#### Housekeeping
# Libraries
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep



#### Code that makes the original creature image on the LED matrix
# Declare colors as RGB values and store them in variables
d = (255, 255, 255) # Cyan
f = (25, 25, 112) # MidnightBlue
g = (0, 191, 255) # DeepSkyBlue
b = (0, 0, 0) # Black

# Arrange colors on an 8x8 matrix to make an image. This is a whale.
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

# Hold the original image on screen for 1 second
sleep(1)



#### Prepare the sensors
# Set up and poll the color sensor
sense.color.gain = 64 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken
rgb = sense.color

#re-assign the whale's eye color variable to the sensed color value
b = (rgb.red, rgb.green, rgb.blue)

# Set up and poll the rotation sensors
orientation = sense.get_orientation_degrees()
roll = orientation["roll"]
pitch = orientation["pitch"]
yaw = orientation["yaw"]
if pitch > 180:
	pitch = pitch - 360

# Starting orientation values
starting_position = roll * 0.1 + pitch * 0.6 + yaw * 0.3
movement = starting_position
direction = "starboard"

# Starting color values
previous_colors = b
modifier = 40 # governs how much the sensor values will be accentuated



#### Create the GIF animation
while True:
	### Color
	# Arrange colors with updated color variable values on 8x8 matrix
	image = [
	  f, f, f, g, g, g, g, g,
	  f, f, g, g, f, g, g, f,
	  f, f, f, f, f, f, g, g,
	  f, g, g, g, g, g, g, g,
	  g, g, g, g, g, g, d, d,
	  g, b, g, g, g, d, d, f,
	  g, g, g, g, d, d, f, f,
	  f, g, g, d, d, f, f, f]
 
	# Code telling the pixels to light up with sensor-based colors
	sense.set_pixels(image)
	
	# Correct the direction if the matrix layout is backwards based on previous loop's orientation
	if direction == "port":
		sense.flip_h()
		
	# Get the color from the sensor
	rgb = sense.color 

	# Accentuate the increases and decreases in RGB values
	current_colors = (rgb.red, rgb.green, rgb.blue) # store the current sensed values for comparison with the previous colors
	changes = [current_colors[0]-previous_colors[0], current_colors[1]-previous_colors[1],current_colors[1]-previous_colors[1]]
	
	# Get the largest and smallest values from the color list
	increase = min(changes)
	decrease = max(changes)
	
	# Determine the position in the list of the max/min values, telling us which colors they represent
	increase_position = changes.index(increase)
	decrease_position = changes.index(decrease)

	# Apply the accentuation
	current_colors_modified = list(current_colors)
	current_colors_modified[increase_position] = current_colors_modified[increase_position] + modifier
	current_colors_modified[decrease_position] = current_colors_modified[decrease_position] - modifier

	# Check that accentuated color values are within correct RGB ranges
	for i in range(3):
		if current_colors_modified[i] > 255:
			current_colors_modified[i] = 255
		if current_colors_modified[i] < 0:
			current_colors_modified[i] = 0
			
	# Convert color values into proper (R, G, B) tuple format from [R, G, B] array format
	b = tuple(current_colors_modified)
	
	# Store this lap's color value for comparison on the next iteration of the loop 
	previous_colors = current_colors
	
	
	### Direction and Rotation
	# Poll the sensors at the start of the loop and store the values in variables
	orientation = sense.get_orientation_degrees()
	roll = orientation["roll"]
	pitch = orientation["pitch"]
	yaw = orientation["yaw"]
	if pitch > 180:
		pitch = pitch - 360
		
	# Get a fresh orientation value for this lap	
	new_movement = roll * 0.1 + pitch * 0.6 + yaw * 0.3
	
	# No direction change or movement if sensor difference is too small
	if abs(movement-new_movement) < 1:
		continue
	
	# Change creature direction to port
	if new_movement < movement and direction == "starboard":
		#sense.flip_h()
		direction = "port"
	
	# Change creature direction to starboard
	if new_movement > movement and direction == "port":
		#sense.flip_h()
		direction = "starboard"
	
	# Compare current orientation to our pre-loop starting orientation
	relative_heel = starting_position - new_movement
	
	# Rotate our creature
	if relative_heel > 4:
		sense.set_rotation(270)
		
	if relative_heel < -4:
		sense.set_rotation(90)
		
	if -4 <= relative_heel <= 4:
		sense.set_rotation(0)
	
	# Store this lap's movement value for comparison on the next iteration of the loop 
	movement = new_movement
	



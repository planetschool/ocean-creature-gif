#### Unfinished ideas for this project

# Trying to rotate the image 45 degrees, determined it is too complex for this project at launch but a good challenge for anyone wanting to go deeper. Image distortion and cropping are likely significant
  
  #Rotate 45 counter clockwise
  rotated_image = []
  '''
  for i in range(0,len(image)):
    if i < 4 or i in range(8,12) or i in range(16, 20) or i in range(24,28):
      if i < 4:
        rotated_image.insert(i, f) 
      else:
        rotated_image.insert(i, image[i-7])
    if i in range(4,8) or i in range(12,16) or i in range(20,24) or i in range(28,32):
      if i == 7 or i == 15 or i == 23 or i == 31:
        rotated_image.insert(i, f) 
      else:
        rotated_image.insert(i, image[i+9])
    if i in range(32,36) or i in range(40,44) or i in range(48,52) or i in range(56,60):
      if i == 32 or i == 40 or i == 48 or i == 56:
        rotated_image.insert(i, f) 
      else:
        rotated_image.insert(i, image[i-9])
    if i in range(36,40) or i in range(44,48) or i in range(52,56) or i in range(60,64):
      if i > 59:
        rotated_image.insert(i, f) 
      else:
        rotated_image.insert(i, image[i+7])
  
  print(len(rotated_image)
  sense.set_pixels(rotated_image)

  for i in range(0,64):
    rotated_image.insert(i, f)
  rotated_image[56] = image[32]
  rotated_image[49] = image[33]
  rotated_image[42] = image[34]
  rotated_image[35] =  image[35]  
  
  rotated_image[40] = image[25]
  rotated_image[33] = image[26]
  rotated_image[26] = image[27]
  
  
  rotated_image[7] = image[31]
  rotated_image[14] = image[30]
  rotated_image[21] = image[29]
  rotated_image[28] = image[28]
  
  
  rotated_image[0] = image[3]
  rotated_image[9] = image[11]
  rotated_image[18] = image[19]
  rotated_image[27] = image[27]
  
  
  rotated_image[63] = image[59]
  rotated_image[54] = image[51]
  rotated_image[45] = image[43]
  rotated_image[36] = image[35]

  #sense.set_pixels(rotated_image)
  '''

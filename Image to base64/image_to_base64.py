'''
Created by: Sumedha Zaware
'''

# Import the required modules
import base64

# Take image file name as input from user
image_file = input()

with open(image_file, "rb") as image:
    base64_string = base64.b64encode(image.read())
print("Base64 string for the selected image is: ", base64_string)

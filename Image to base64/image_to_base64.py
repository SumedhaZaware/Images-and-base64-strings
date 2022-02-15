'''
Created by: Sumedha Zaware
'''

# Import the required modules
import base64

# Take image file name as input from user
image_file = input()

with open(image_file, "rb") as image:
    base64_string = str(base64.b64encode(image.read()))

output_file = open("base64_output.txt", "w") 
output_file.write(base64_string)
output_file.close()
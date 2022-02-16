'''
Created by: Sumedha Zaware
'''

import base64

base64_str = open('base64_str.txt', 'rb')
byte_format = base64_str.read()
base64_str.close()

decode_to_img = open('Converted_image.jpeg', 'wb')
decode_to_img.write(base64.b64decode((byte_format)))
decode_to_img.close()

#!/usr/bin/python

import requests
# IF YOU NEED TO INSTALL THE MODULE: $ sudo apt-get install python-requests
#                            AND/OR  $ pip install requests
#                                    $ pip3 install requests

import base64
import json

# Sample image file is available at http://plates.openalpr.com/ea7the.jpg (country=us)
# IMAGE_PATH = './tmp/ea7the.jpg'
IMAGE_PATH = './tmp/sample.jpg'
SECRET_KEY = 'sk_XXXXXXXXXX'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=eu&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)

print(json.dumps(r.json(), indent=2))

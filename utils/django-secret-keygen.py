#!/usr/bin/env python3
''' Courtesy of https://gist.github.com/9205591.git
    This script will print a unique key for your local django build.
    Add this key to settings_secrets.py
'''

import string
import random
 
# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
 
SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])
 
print("\'%s\'" %SECRET_KEY)

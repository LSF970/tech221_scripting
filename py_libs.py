# Python Libraries and Modules

# Extensive libraries in Python - External collections of useful functions and methods

# Python comes with some integrated libraries

from random import *
import math

print(random())

num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)

# Modules
import os
import datetime, sys

working_dir = os.getcwd()
print(working_dir)

print(datetime.date.today())

print(sys.path)

def operating_system_information():
    print(os.cpu_count())

operating_system_information()

# pip - pythons package manager
import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc.content)




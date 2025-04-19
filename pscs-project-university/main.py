# TODO: Remove unwanted code
# TODO: check every column on every screen especially status to make sure they respresent what they are supposed to represent

import os
import sys

base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
print(base_path)

if os.path.isfile(base_path):
    print(f"{base_path} is a file.")
elif os.path.isdir(base_path):
    print(f"{base_path} is a directory.")
else:
    print(f"{base_path} does not exist or is not a valid path.")

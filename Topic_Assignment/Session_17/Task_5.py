# Set up a new virtual environment using venv, activate it, and install 
# the 'requests' package using pip. Write a short script that imports requests 
# and prints the version installed.
# Hint: Use 'python -m venv venv_folder', then 'pip install requests'.

import requests

print("Requests Package Version:")
print(requests.__version__)

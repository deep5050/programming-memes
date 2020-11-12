import json
from urllib.request import urlopen
import os
import re
import pickle
import requests
import shutil
from time import sleep

ids = [1944,1945,1946,1947,1948,1949]

with open('ids.data', 'wb') as filehandle:
    # store the data as binary data stream
    pickle.dump(sorted(ids), filehandle)


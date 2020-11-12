import json
from urllib.request import urlopen
import os
import re
import pickle
import requests
import shutil
from time import sleep

ids = []


url = 'https://tg.i-c-a.su/json/programmerjokes/2?limit=100'
r = urlopen(url)
data = json.loads(str(r.read().decode("utf-8")))


with open('ids.data', 'rb') as filehandle:
    # read the data as binary data stream
    ids = pickle.load(filehandle)


for message in data['messages']:
    #print(message['id'])
    id = message['id']

    # check if already in the database
    if int(id) in ids:
        print(str(id)+': already in the database')
        continue

    # download image
    img_url = 'https://tg.i-c-a.su/media/programmerjokes/'+str(id)
    response = urlopen(img_url)
    img_file = open('memes/'+str(id)+'.png','wb')
    img_file.write(response.read())
    img_file.close()
    print(str(id)+': downloaded')
    sleep(2)
    ids.append(int(message['id']))


with open('ids.data', 'wb') as filehandle:
    # store the data as binary data stream
    pickle.dump(sorted(ids), filehandle)

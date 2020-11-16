from os import listdir
from os.path import isfile, join
import json
from PIL import Image
import os

memes = []
invalid_images = []
mypath = "memes/3"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    try:
        temp = {}
        with Image.open('./'+mypath+'/'+file) as img:
            width, height = img.size

        temp['id'] = file.split('.')[0]
        temp['path'] = mypath+'/'+file
        temp['width'] = width
        temp['height'] = height
        memes.append(temp)
    except:
        print(file, 'is not a valid image !')
        invalid_images.append('./'+mypath+'/'+file)
        # delete file


for invalid in invalid_images:
    os.remove(invalid)
    print(invalid ," removed")
    
f = open('3.json', 'w')
f.write(json.dumps(memes))
f.close()

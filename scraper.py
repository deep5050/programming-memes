#!/usr/bin/env python3
import configparser
import argparse
import json
from urllib.request import urlopen
import os
import re

version = '1.0.0'

parser = argparse.ArgumentParser(description='Download attachments by file names by a Telegram Channel')
parser.add_argument('--config', help='Config file', nargs='?', action='store', const='', default=os.path.abspath(os.path.dirname(__file__)) + '/config.ini')
args = parser.parse_args()

print('DL-Telegram-by-file-attachment started...')

if args.config is not None:
    if not os.path.exists(args.config):
        print('Config file not found on ' + args.config)
        exit()
    print('  Config loaded!')
    config = configparser.RawConfigParser()
    config.read_file(open(args.config))
else:
    if not os.path.exists('config.ini'):
        print('Config file not found')
        exit()

channel_name = str(config.get('channel', 'name')).lower()
pages = int(config.get('channel', 'pages'))

for page in range(1,pages):
    print('Parsing ' + str(page) + ' page')
    url = 'https://tg.i-c-a.su/json/' + channel_name + '/' + str(page) + '?limit=100'
    r = urlopen(url)
    data = json.loads(str(r.read().decode("utf-8")))

    search = str(config.get('channel', 'filter'))
    search = search.split(',')

    for message in data['messages']:
        if 'media' in message:
            for term in search:
                if 'document' in message['media'] and re.search(term, message['media']['document']['attributes'][0]['file_name'], re.IGNORECASE):
                    print(' Download ' + message['media']['document']['attributes'][0]['file_name'])
                    if not os.path.exists(config.get('channel', 'download') + message['media']['document']['attributes'][0]['file_name']):
                        try:
                            response = urlopen('https://tg.i-c-a.su/media/' + channel_name + '/' + str(message['id']))
                            file = open(config.get('channel', 'download') + message['media']['document']['attributes'][0]['file_name'], 'wb')
                            file.write(response.read())
                            file.close()
                        except:
                            print('  Too many requests to the service')
                            print('  https://tg.i-c-a.su/media/' + channel_name + '/' + str(message['id']))

print('Downloading terminated')

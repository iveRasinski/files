import os
import requests
import time
import requests
from bs4 import BeautifulSoup
import json
# pip: pygame

def writeDate(source, value):
    with open("config.json") as file:
        data = json.load(file)
    data[source] = value
    with open("config.json", "w+") as newfile:
        json.dump(data, newfile, indent=4)
    file.close()
    newfile.close()

def readDate():
    with open("config.json") as file:
        data = json.load(file)
    file.close()
    return data

run = True
while run:
    time.sleep(10)
    try:
        reqUrl = requests.get('https://raw.githubusercontent.com/Nikoomitk/dbd/main/test.txt')
        data = BeautifulSoup(reqUrl.content, 'html.parser').text.replace('# ', '').replace('\n', ':').split(':')
        dates = readDate()

        if data[0] != dates["shutdown"]:
            os.system("shutdown /s /t 0")
            writeDate("shutdown", data[0])

        if data[1] != dates["sound"]:
            from os import environ
            environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
            from pygame import mixer
            mixer.init()
            mixer.music.load('sound.mp3')
            mixer.music.play()
            time.sleep(5)
            mixer.music.stop()
            writeDate("sound", data[1])

        if data[2] == "exit":
            run = False
    except:
        pass
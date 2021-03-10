import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,fileName):
    pass

def mergeAudios(audios):
    pass

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 88000
    finish = 90200
    audioprocessed = audio[start:finish]
    audioprocessed.export("1_hindi.mp3",format="mp3")



def generateAnnouncement(fileName):
    pass

if __name__ == "__main__":
    generateSkeleton()
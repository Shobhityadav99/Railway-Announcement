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



    start = 91000
    finish = 92200
    audioprocessed = audio[start:finish]
    audioprocessed.export("3_hindi.mp3",format="mp3")

    start = 94000
    finish = 95000
    audioprocessed = audio[start:finish]
    audioprocessed.export("5_hindi.mp3",format="mp3")



def generateAnnouncement(fileName):
    pass

if __name__ == "__main__":
    generateSkeleton()
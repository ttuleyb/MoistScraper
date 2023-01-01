# Scrape transcripts from youtube
from pytube import YouTube
import requests
import re
import time

def getTranscript(url):
    yt = YouTube(url)

    captions = yt.captions.all()
    try:
        captionUrl = captions[0].url
    except:
        time.sleep(3)
        captions = yt.captions.all()
        captionUrl = captions[0].url

    # Download the captions
    captionData = requests.get(captionUrl).text

    # Format the captions XML

    import xml.dom.minidom
    dom = xml.dom.minidom.parseString(captionData)

    words = dom.getElementsByTagName('s')

    allWords = ""

    for word in words:
        #print(word.firstChild.nodeValue)
        allWords += word.firstChild.nodeValue + " "
        
    # Remove double spaces
    allWords = allWords.replace("  ", " ")
    
    # Get the name of the video
    videoName = yt.title
    
    return allWords, videoName
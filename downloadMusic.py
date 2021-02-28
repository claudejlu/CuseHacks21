import urllib.request
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import youtube_dl

def downloadMP3(link, filename):
    options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl': "/Users/claudelu/Desktop/CuseHacks21/static/{}.%(ext)s".format(filename),     #name the file the ID of the video
    'noplaylist':True,
    'nocheckcertificate':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
# 'http://www.youtube.com/watch?v=BaW_jenozKc'
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([link])

def findYoutubeLink(search_keyword):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]


# print(downloadMP3('https://www.youtube.com/watch?v=yKNxeF4KMsY&ab_channel=Coldplay', "YellowColdPlay"))
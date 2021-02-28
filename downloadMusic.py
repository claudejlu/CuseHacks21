import youtube_dl
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl': "/Users/claudelu/Desktop/CuseHacks21/" + "%(ext)s.",     #name the file the ID of the video
    'noplaylist':True,
    'nocheckcertificate':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

# 'http://www.youtube.com/watch?v=BaW_jenozKc'
def downloadMP3(yt_url):
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([yt_url])

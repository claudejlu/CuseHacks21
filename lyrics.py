import lyricsgenius as genius

token = "-dQUYTvZAaAlhnZs6WaYxcXBdbYc1d1VhBWAGraj34Mm1pyhE1Bp28U55ygTBBrc"
genius = genius.Genius(token)

def getLyrics(songName):
    song = genius.search_song(songName)
    return song.lyrics
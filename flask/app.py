from flask import Flask, request
import os

app = Flask(__name__)

queue = []

class Song:
    
    def __init__(self, provider, link):
        self.provider = provider
        self.link = link

        #Set name, artist, length, picture based on provider
        if self.provider == "spotify":
            self.setSpotifyData()
        if self.provider == "youtube":
            self.setYoutubeData()
        if self.provider == "soundcloud":
            self.setSoundcloudData()

    def play(self):
        if self.provider == "spotify":
            self.playSpotify()
        if self.provider == "youtube":
            self.playYoutube()
        if self.provider == "soundcloud":
            self.playSoundcloud()
    
        
    def playSpotify(self):
        #Spotify API implementation
        print("spotify")

    def playYoutube(self):
        #Youtube API implementation
        print("Youtube")

    def playSoundcloud(self):
        #Youtube API implementation
        print("Soundcloud")

    def setSpotifyData(self):
        print("Spotify data")

    def setYoutubeData(self):
        print("Youtube data")

    def setSoundcloudData(self):
        print("Soundcloud data")


@app.route('/queue/get')
def get_queue():
    return {queue}

@app.route('/queue/post')
def add_song():
    song_request = request.get_json()
    queue.append(Song(song_request['provider'], song_request['link']))

    return{
        "statusCode":200,
        "message": "Song added to queue"
    }

@app.route('/queue/delete')
def delete_song():
    response = request.get_json()
    deleted_song = queue.pop(response['index'])
    return{
        "statusCode":200,
        "message": ("%s removed from queue", deleted_song.name)
    }
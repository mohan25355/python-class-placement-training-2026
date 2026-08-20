class playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
        print(f"Song '{song}' added to playlist '{self.name}'.")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Song '{song}' removed from playlist '{self.name}'.")
        else:
            print(f"Song '{song}' not found in playlist '{self.name}'.")
    def show_songs(self):
            for song in self.songs:
                print(f"- {song}")
my_playlist=playlist("My Favorite Songs")
my_playlist.add_song("amma songs")
my_playlist.add_song("vanakam chennai")
my_playlist.show_songs()
my_playlist.remove_song("amma songs")
my_playlist.show_songs()
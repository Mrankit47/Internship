class playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []
    def add_song(self,song):
        self.songs.append(song)
        print(f"Added {song}")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed {song}")
    def show_songs(self):
        print(f"Playlist '{self.name}'")
        for song in self.songs:
            print(f"{song}")
my_songs = playlist("Favorites")
my_songs.add_song("teri aakhe")
my_songs.add_song("humsafar")
my_songs.add_song("dosti")
my_songs.add_song("hwaye")

my_songs.show_songs()

my_songs.remove_song("humsafar")
my_songs.remove_song("hwaye")

my_songs.show_songs()
class Song(object):

    def __init__(self, lyrics): # create the mini-module 'self' that contains the lyrics
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


bday_song = ("Happy birthday to you",
            "I don't want to get sued",
            "So I'll stop right there")
happy = Song(bday_song)
happy.sing_me_a_song()
#happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

#happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

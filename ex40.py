class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

up = Song(["I was down, but now I'm up, yeah","This all God, this ain't no luck, yeah", "I used to be stuck in that mud, wow", "Yeah, I was down, but now I'm up, up, up, up"])

up.sing_me_a_song()
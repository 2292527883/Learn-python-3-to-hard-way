
import my

mystuff = {'apple': 'I an apples !'}

print(mystuff['apple'])


my.apple()
print(my.tangerine)


class fuck(object):

    def __init__(self):
        self.a = "And now a thousand years between"

    def apple(self):
        print("I am Class apples !")


things = fuck()
things.apple()

print(things.a)


class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            print("*" * 100)


happy_bday = song(["Happy birthday to you",
                   "I don't want to get sued , ", "So  I'll stop right there"])
bulls_on_parade = song(["They rally around the family",
                        "With pocket full of sheels"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

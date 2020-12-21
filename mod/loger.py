import os, time

"""The logging in Python is too complex to use..."""

class loger:

    """A nice logger QWQ"""

    def __init__(self):
        if not os.path.exists("logs"):
            os.mkdir("logs")
        self.flhd = open("./logs/" + str(time.time()) + ".log", "w", encoding='utf-8')

    def log(self, *tar, doTellUser = False):
        tar = "; ".join(tuple(str(x) for x in tar))
        self.flhd.write(str(time.ctime()) + ': ' + tar + '\n')
        if doTellUser:
            print(tar)
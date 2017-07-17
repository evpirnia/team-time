class Person:
    def __init__(self):
        self.free = []
        self.lastfree = 0
    def addBusy(self, busy_start, busy_end):
        if busy_start != 0:
            self.free.append([self.lastfree, busy_start])
        self.lastfree = busy_end
    def getFree(self):
        if self.lastfree < 23:
            self.free.append([self.lastfree, 23])
        self.lastfree = 23
        return self.free

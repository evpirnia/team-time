input = [[0, 4], [5, 9], [10, 14]], [[6, 9], [15, 17]], [[3, 9]]

persons = []
free_overall = []
result = []

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

for person in input:
    new_person = Person()
    for [start_time, end_time] in person:
        new_person.addBusy(start_time, end_time)
    persons.append(new_person)

for person in persons:
    free_times = person.getFree()
    for [start, end] in free_times:
        for i in range(start, end):
            free_overall.append(i)

free_overall = list(set([x for x in free_overall if free_overall.count(x) == len(persons)]))

last = free_overall[0]
size = len(free_overall)
for i in range(size-1):
    next = free_overall[i+1]
    current = free_overall[i]
    if next - current != 1:
        result.append([last, current + 1])
        last = free_overall[i+1]

result.append([last, next+1])

print(result)

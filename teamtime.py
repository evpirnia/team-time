from person import Person

class TeamTime:
    def __init__(self):
        self.input = []
        self.persons = []
        self.free_times = []
    def read(self, filename):
        temp = []
        with open(filename, "r") as file_open:
            for line in file_open:
                line = line.replace("\n", "")
                if len(line) > 0:
                    temp += [tuple(map(int, line.split(',')))]
                else:
                    self.input.append(temp)
                    temp = []
        self.input.append(temp)
    def get(self):
        temp = []
        for person in self.input:
            new_person = Person()
            for [start_time, end_time] in person:
                new_person.addBusy(start_time, end_time)
            self.persons.append(new_person)
        for person in self.persons:
            free_times = person.getFree()
            for [start, end] in free_times:
                for i in range(start, end):
                    temp.append(i)
        temp = list(set([x for x in temp if temp.count(x) == len(self.persons)]))
        last = temp[0]
        size = len(temp)
        for i in range(size-1):
            next = temp[i+1]
            current = temp[i]
            if next - current != 1:
                self.free_times.append([last, current + 1])
                last = temp[i+1]
        self.free_times.append([last, next+1])
        return self.free_times

import csv

class Iterator:
    def __init__(self, label, file) -> None:
        self.label = label
        self.file = file
        self.score = 0
        self.data = []
        with open(self.file_name) as reading_file:
            file_reader = csv.reader(reading_file, delimiter=";")
            for i in file_reader:
                self.data.append(i[0])
            self.limit = len(self.data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            i = self.counter
            self.counter += 1
            return self.data[i]
        else:
            raise StopIteration
    
    
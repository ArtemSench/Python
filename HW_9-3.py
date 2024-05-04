class EvenNumbers:

    def __init__(self, start, end):
        self.i, self.start, self.end = 0, start, end
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i = self.start - 1
        self.i += 1
        if self.i > self.end:
            raise StopIteration
        if self.i % 2 == 0:
            return self.i
        if self.i % 2 == 1:
            self.i +=1


en = EvenNumbers(10, 25)
for i in en:
    print(i)
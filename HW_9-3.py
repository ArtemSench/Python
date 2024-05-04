class EvenNumbers:

    def __init__(self, start, end):
        self.i, self.start, self.end = start - 1, start, end
    def __iter__(self):
        self.i = self.start - 1
        return self
    def __next__(self):
        self.i += 1
        if self.i % 2 == 0:
            if self.i > self.end:
                raise StopIteration
            return self.i
        if self.i % 2 == 1:
            return ''


en = EvenNumbers(10, 25)
for i in en:
    print(i)

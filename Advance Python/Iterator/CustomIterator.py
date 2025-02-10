class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        else:
            raise StopIteration
        
c = Counter(5)
#We can use both ways
print(next(c))
print(c.__next__())
print(next(c))
print(c.__next__())
print(next(c))
print(next(c))
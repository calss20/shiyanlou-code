#!/usr/bin/env python3
def my_generator():
    print("Inside my geneator")
    yield 'a'
    yield 'b'
    yield 'c'

my_generator()
c = my_generator()
dir(c)

for char in my_generator():
    print(char)


def countr_generator(low, high):
    while low <= high:
        yield low
        low += 1

for i in countr_generator(5,10):
    print(i, end=' ')

def infinite_generator(start=0):
    while True:
        yield start
        start += 1

for num in infinite_generator(4):
    print(num, end=' ')
    if num > 20:
        break

class Counter(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        counter = self.low
        while self.high >= counter:
            yield counter
            counter += 1

gobj = Counter(5, 10)
for num in gobj:
    print(num, end=' ')

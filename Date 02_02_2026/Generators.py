''' A generator is a simpler way to create 
an iterator using:
yield keyword
no need for __iter__() or __next__() '''

def count(limit):
    num = 1
    while num<=limit:
        yield num
        num += 1
for i in count(5):
    print(i)

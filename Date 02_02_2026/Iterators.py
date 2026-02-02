# Iterator is an object that can be iterated (looped) one value at a time.
# use __iter__() and __next__() methods.

# working

number = [1, 2, 3]

it = iter(number)

print(next(it))
print(next(it))
print(next(it))
print(next(it))  # when values finish StopIteration error
# when values finish StopIteration error
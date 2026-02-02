def myfun(n):
    return lambda b : n *b
c = myfun(3)
print(c(2))
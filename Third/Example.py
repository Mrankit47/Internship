Sen = "ankit anuj ansh aakash ajay anuj ansh ajay"

allwords = Sen.lower().split()
rep ={}
for word in allwords:
    rep[word]=rep.get(word,0)+1
print(rep)

sentence = '''Python programming
              web devlopment
              python django
              web with django Python in Programming Language  '''

words = sentence.upper().split()
print(words)
freq = {}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
    # freq[word] = freq.get(word, 0) + 1

print(freq)



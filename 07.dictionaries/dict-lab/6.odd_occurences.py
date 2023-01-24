words = input().split()
words = list(map(lambda w: w.lower(), words))
occurences = {}
for word in words:
    if word not in occurences:
        occurences[word] = 1
    else:
        occurences[word] += 1

odd_words = []
for word in occurences:
    if occurences[word] % 2 != 0:
        odd_words.append(word)

print(" ".join(odd_words))

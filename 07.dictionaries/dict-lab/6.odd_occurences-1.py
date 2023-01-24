words = input().split()
occurences = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in occurences:
        occurences[word_lower] = 1
    else:
        occurences[word_lower] += 1

for word_lower in occurences:
    if occurences[word_lower] % 2 != 0:
        print(word_lower, end = " ")
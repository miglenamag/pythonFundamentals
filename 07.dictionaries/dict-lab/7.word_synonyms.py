count = int(input())

synonyms_dict = {}
for _ in range(count):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = list()
    synonyms_dict[word].append(synonym)
for word in synonyms_dict:
    synonyms = ", ".join(synonyms_dict[word])
    print(f"{word} - {synonyms}")



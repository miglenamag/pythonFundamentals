import re

n=int(input())
pattern = r'!\b([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

for _ in range(n):
    message = input()
    match = re.search(pattern, message)

    if not match:
        print(f"The message is invalid")
    else:
        command,text = match.groups()
        print(f'{command}: ',end='')
        translated_text = [str(ord(ch)) for ch in text]
        print(" ".join(translated_text))


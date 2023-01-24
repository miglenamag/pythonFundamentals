import re

n = int(input())
pattern = r'^!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'
for _ in range(n):
    command = input()
    check = re.findall(pattern,command)
    if check == []:
        print("The message is invalid")
    else:
        print(f'{check[0][0]}: ',end='')
        ascii_nums = [str(ord(ch)) for ch in check[0][1]]
        print(' '.join(ascii_nums))
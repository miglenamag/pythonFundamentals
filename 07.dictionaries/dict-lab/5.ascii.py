character = input().split(", ")
#char_dict ={}
char_dict = {char:ord(char) for char in character}
#for char in character:
   # char_dict[char] =ord(char)

print(char_dict)

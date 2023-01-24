number = int(input())
search_word = input()
list_of_strings = []
for i in range(number):
    list_of_strings.append(input())
print(list_of_strings)
filtered=[]
for  current_string in list_of_strings:
    if search_word in current_string:
        filtered.append(current_string)
print(filtered)

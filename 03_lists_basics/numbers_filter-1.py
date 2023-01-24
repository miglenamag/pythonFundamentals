n = int(input())
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
filter_command = input()
if filter_command == "even":
    print (even_numbers)
elif filter_command == "odd":
    print (odd_numbers)
elif filter_command == "negative":
    print (negative_numbers)
elif filter_command == "positive":
    print (positive_numbers)




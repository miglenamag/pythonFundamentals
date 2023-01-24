n = int(input())
even = []
odd = []
positive = []
negative = []

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

# commands are even odd positive negative
filter_command = input()
print(eval(filter_command))




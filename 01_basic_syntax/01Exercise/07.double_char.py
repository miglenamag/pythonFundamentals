command = input()

while command != "End":
    if command != "SoftUni":
        for char in command:
            print(char*2, end='')
        command = input()
        print()
    else:
        command = input()
word = input()
line = input()
while line != "End":
    command = line.split()
    if command[0] == "Translate":
        print(word.replace(command[1], command[2]))

    elif command[0] == "Includes":
        if command[1] in word:
            print("Тrue")
        else:
            print("False")
    elif command[0] == "Start":
        if word.startswith(command[1]):
            print("Тrue")
        else:
            print("False")
    elif command[0] == "Lowercase":
        print(word.lower())
    elif command[0] == "FindIndex":
        print(word.rfind(command[1]))
    elif command[0] == "Remove":
        print(word[int(command[1])+int(command[2])::])

    line = input()




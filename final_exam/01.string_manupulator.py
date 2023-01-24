string = input()
command = input()
while command!='End':
    command_list = command.split()
    if command_list[0] == 'Translate':
        string = string.replace(command_list[1],command_list[2])
        print(string)
    elif command_list[0] == 'Includes':
        print(command_list[1] in string)
    elif command_list[0] == 'Start':
        print(string.find(command_list[1])==0)
    elif command_list[0] == 'Lowercase':
        string = string.lower()
        print(string)
    elif command_list[0] == 'FindIndex':
        index = string.rfind(command_list[1])
        print(index)
    elif command_list[0] == 'Remove':
        startIndex = int(command_list[1])
        count = int(command_list[2])
        to_remove = string[startIndex:startIndex+count]
        string = string.replace(to_remove,'')
        print(string)
    command = input()
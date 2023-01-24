def reverseLookup(dict_arg, values):
    return [key for key in dict_arg if dict_arg[key] == values]


names = {'Ali': 20, 'Marina': "email", 'George': 16, 'Other': 16}
msg = input('enter age:\t')
print(reverseLookup(names, msg))

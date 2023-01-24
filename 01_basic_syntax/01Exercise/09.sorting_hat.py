name = " "
flag = False
while name != "Welcome!":
    name = input()
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6 and name != "Voldemort" and name != "Welcome!":
        print(f"{name} goes to Hufflepuff.")
    elif name == "Voldemort":
        flag = True
        print(f"You must not speak of that name!")
        break
if not flag:
    print(f"Welcome to Hogwarts.")

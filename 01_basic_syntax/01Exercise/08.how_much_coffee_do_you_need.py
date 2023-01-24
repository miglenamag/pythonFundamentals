command = ""
needed_coffees = 0
while command.lower() != "end":
    command = input()
    if command.lower() == "coding" or command.lower() == "dog" \
            or command.lower() == "cat" or command.lower() == "movie":
        # if any(l.isupper() for l in command): Ne minavat vsichki v Judge
        if command.islower():
            needed_coffees += 1
        else:
            needed_coffees += 2

if needed_coffees > 5:
    print(f"You need extra sleep")
else:
    print(needed_coffees)

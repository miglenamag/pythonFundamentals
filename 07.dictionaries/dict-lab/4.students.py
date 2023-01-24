text = input()
courses = dict()

while ":" in text:
    #data = text.split(":")  # връща списък от 3 елемента name, id, course
    #name = data[0]
    #id = data[1]
    #course = data[2]

# горните 4 реда могат да се заменят с tuple,
    # /като не е задължително променливите от tuple да се захраждат в скоби,
    # / както е показано в лекцията на А.Георгиев :
    # (name, id, course) = text.split(":")
    name, id, course = text.split(":")
    if course not in courses.keys():
        courses[course] = dict()
# създавам нов речник, ако не съществува този курс с ключ итерирания course и стойност вложен речник, който съдържа името на студента и неговото ID за съответния записан курс

    courses[course][id] = name
# ключът на вложения речник е Id на студента, а стойността е неговия name

    text = input()

#text = text.replace("_", " ")
# замяната може да се направи и чрез split и join
text = " ".join(text.split("_"))

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")
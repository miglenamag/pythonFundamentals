usernames = input().split(", ")
for username in usernames:
    username_is_valid = True
    if not 3 <= len(username) <= 16:
        username_is_valid = False
        continue
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            username_is_valid = False
        continue
    if " " in username:
        username_is_valid = False

    if username_is_valid:
        print(username)
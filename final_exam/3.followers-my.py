line = input()
followers = {}

while line != "Log out":
    commands = line.split(": ")
    username = commands[1]
    if commands[0] == "New follower":
        if username not in followers:
            followers[username] = [0, 0]
    elif commands[0] == "Like":
        likes = int(commands[2])
        if username not in followers:
            followers[username] = [likes, 0]
        else:
            followers[username][0] += likes
    elif commands[0] == "Comment":
        if username not in followers:
            followers[username] = [0, 1]
        else:
            followers[username][1] += 1
    elif commands[0] == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]
    line = input()

print(f"{len(followers)} followers")
for username in followers:
    all_likes_comments=followers[username][0] +followers[username][1]
    print(f"{username}: {all_likes_comments}")

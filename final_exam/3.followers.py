line = input()
facebook = {}
while line!='Log out':
    line_list = line.split(': ')
    username = line_list[1]
    if line_list[0] == 'New follower':
        if username not in facebook:
            facebook[username] = {'likes':0,'comments':0}
    elif line_list[0] == 'Like':
        likes = int(line_list[2])
        if username not in facebook:
            facebook[username] = {'likes':likes,'comments':0}
        else:
            facebook[username]['likes'] += likes
    elif line_list[0] == 'Comment':
        if username not in facebook:
            facebook[username] = {'likes': 0, 'comments': 1}
        else:
            facebook[username]['comments']+=1
    elif line_list[0] == 'Blocked':
        if username not in facebook:
            print(f"{username} doesn't exist.")
        else:
            del facebook[username]
    line = input()
print(f'{len(facebook)} followers')
for username in facebook:
    print(f'{username}: {facebook[username]["likes"]+facebook[username]["comments"]}')
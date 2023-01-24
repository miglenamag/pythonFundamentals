my_list = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    min_number = min(my_list)
    my_list.remove(min_number)
for index in range(len(my_list)):
    if index == len(my_list) - 1:
        print(f"{my_list[index]}")
    else:
        print(f'{my_list[index]},',end =" ")



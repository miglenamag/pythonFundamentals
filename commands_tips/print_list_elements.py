list = [1, 2, 3]
# print(list) #printed list with[]

# printed elements of list divided with interval
# 1
# for element in list:
#     print(element, end=" ")
# 2
# for index in range(len(list)):
#     print(list[index], end=" ")

# after the last element prints ,
# for index in range(len(list)):
#   print(f"{list[index]},", end=" ")

# without the last , in printed list
# for index in range(len(list)):
#     if index == len(list) - 1:
#         print(f"{list[index]}",end = "")
#     else:
#         print(f"{list[index]},",end=" ")

# all above can be substitued with unpacking - prints elements with spaces between each
print(*list)

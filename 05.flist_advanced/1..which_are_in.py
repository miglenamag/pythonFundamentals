list1 = input().split(", ")
list2 = input().split(", ")
substring = [x for x in list1 if any(x in w for w in list2)]
print(substring)
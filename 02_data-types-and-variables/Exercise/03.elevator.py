# n = int(input())
# p = int(input())
# if n > p:
#     if n % p != 0:
#         courses = n // p
#         remainder = n % p
#         print(f"{courses} courses * {p} people")
#         print(f"+ 1 course * {remainder} persons")
#     else:
#         courses = n // p
#         print(f"{courses} courses * {p} people")
# else:
#     print(f"All the persons fit inside the elevator.")
#     print("Only one course is needed.")

n = int(input())
p = int(input())
if n % p == 0:
    courses = n // p
else:
    courses = n // p + 1
print(courses)

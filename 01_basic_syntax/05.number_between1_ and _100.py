is_between = False
while  not is_between:
    num = float(input())
    if 1 <= num <= 100:
        is_between = True
        print(f"The number {num} is between 1 and 100")

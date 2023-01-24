number = float(input())
if number != 0:
    if number > 0:
        if 1 < number < 1000000:
            print(f"Number is positive")
        else:
            if number > 1000000:
                print(f"Number is  large positive")
            else:
                print(f"Number is  small positive")
    else:
        if 1 < abs(number) < 1000000:
            print(f"Number is negative")
        else:
            if abs(number) > 1000000:
                print(f"Number is  large negative")
            else:
                print(f"Number is  small negative")
else:
    print(f"Number is zero")

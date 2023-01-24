numbers = [2, 4, 6, 8, 10]

def square_number(number):
    return number * number
square_numbers = list(map(square_number, numbers))
print (square_numbers)

def check_numbers(num)
    if num %2 == 0:
        return True
    else:
        return False

result = list(filter(check_numbers, numbers))
print (result)

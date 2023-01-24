# def convert_to_int(el):
#     return int(el)



nums_as_string = ["1", "2", "3"]

# numbers = [int(el) for el in nums_as_string]
# numbers = [convert_to_int(el) for el in nums_as_string]
# numbers = list(map(int, nums_as_string))
# numbers = list(map(lambda el:int(el),nums_as_string))
numbers = []
for num in nums_as_string:
    numbers.append(int(num))

# even = [el for el in numbers if el % 2 == 0]
even = list(filter(lambda el: el % 2 == 0, numbers))
print(numbers)
print(even)

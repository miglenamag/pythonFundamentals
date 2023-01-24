import timeit


# timeit - библиотека чрез която може да се извиква времето за изпълнение на дадена операция

def even_numbers_with_comprehension():
    return [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]


def even_numbers_with_loop():
    even_nums = []

    for num in [1, 2, 3, 4, 5, 6]:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

print(even_numbers_with_comprehension())
print("Execution time with list comprehension:")
print(timeit.timeit())

print(even_numbers_with_loop())
print("Execution time with loop:")
print(timeit.timeit())

# Примерът с list comprehension се изпълнява за по-кратко време
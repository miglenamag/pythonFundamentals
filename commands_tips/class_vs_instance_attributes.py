class Test:
    print("seting class attribute")
    value = 52

    def __init__(self):
        self.value = 42

print (f"This is class attribute {Test.value}")
obj = Test()
print (f"This is instance attribute {obj.value}")
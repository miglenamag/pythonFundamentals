number = int(input())

positives = []
negatives = []
for i in range(number):
    current_num = int(input())
    if current_num >= 0:
        positives.append(current_num)
    else:
        negatives.append(current_num)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

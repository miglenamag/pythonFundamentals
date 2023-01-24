import math

biscuites_per_day = int(input())
count_of_workers = int(input())
competing_production = int(input())
count_of_biscuits = 0

for day in range(1, 31):
    if day % 3 == 0:
        count_of_biscuits += math.floor(count_of_workers * biscuites_per_day * 75 / 100)
    else:
        count_of_biscuits += count_of_workers * biscuites_per_day
diff = abs(count_of_biscuits - competing_production)
percentage = diff / competing_production * 100
print(f" You have produced {count_of_biscuits} biscuits for the past month.")
if count_of_biscuits > competing_production:
    print (f'You produced {percentage:.2f} percent more biscuites.')
else:
    print(f'You produced {percentage:.2f} percent less biscuites.')
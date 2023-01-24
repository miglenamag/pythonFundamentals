divisor = int(input())
boundary = int(input())
is_found = False
for i in range(boundary, divisor-1, -1): # from boundary to divisor
    if i % divisor == 0:
        is_found = True
        N = i
        break
if is_found:
    print(N)
else:
    print(f'Not found')

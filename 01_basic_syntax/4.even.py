n=int(input())
#flag=True
for i in range(n):
    current=int(input())
    if current % 2 != 0:
        print(f"{current} is odd!")
        #flag=False
        break
#if flag:
    #print("All numbers are even.")
else:
    print("All numbers are even.")
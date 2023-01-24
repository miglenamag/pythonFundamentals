# 1
# tail = input()
# body = input()
# head = input()
# meerkat = [head, body, tail]
# 2
# meerkat = [tail, body, head]
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
# print(meerkat)

# 3
meerkat = []
meerkat.append(input())
meerkat.append(input())
meerkat.append(input())
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)

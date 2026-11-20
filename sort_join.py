a = [33, 7, 21]
b = sorted(a)
print(a, b)

r = a.sort()
print(a, r)
print(sorted(a, reverse=True))

print(', '.join(['사과', '배', '감']))
print('-'.join(['2026', '11', '08']))

nums= [3, 15, 22]
strs = []

for n in nums :
    strs.append(str(n))

print(strs)
print(' -'.join(strs))
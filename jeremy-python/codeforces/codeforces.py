a = input()
b = []
print b
for x in range(a):
    b.append(raw_input().split(' '))
d = {}
for k,v in b:
    d[k] = int(v) + int(d.get(k, 0))
print d
inverse = [(value, key) for key, value in d.items()]
print inverse
max_key = max(inverse)[1]
print max_key
max_val = d.get(max_key, v)
print max_val
d = {}
for k,v in b:
    d[k] = int(v) + int(d.get(k, 0))
    if d[k] == max_val:
       answer = k
       break
print answer
    
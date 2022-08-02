# Put your code here
filename = input('Enter the input file name: ')
d = {}
with open(filename, 'r') as f:
    for line in f:
        for word in line.strip().split():
            if word not in d:
                d[word] = 0
            d[word] += 1
items = list(d.items())
items.sort()
print()
for k, v in items:
    print(k, v)

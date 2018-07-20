import re


b = input("input=")
pattern = r'"\w+"\}'
c = []
a = re.findall(pattern, b)
for i in range(len(a)):
    c.append(a[i][:-1])

print(c)
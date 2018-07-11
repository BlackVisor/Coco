import re

with open(r"C:\Users\Oujia\Documents\Tencent Files\812264061\FileRecv\new 3.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
pattern = r'productPrice":"\d+\.\d+"'
c = a[0]
b = re.findall(pattern, c)
pattern1 = r'\d+\.\d+'
for i,j in enumerate(b):
    d = re.findall(pattern1, j)
    if float(d[0]) > 0.01 or float(d[0]) < 99999.9999:
        print(d[0])

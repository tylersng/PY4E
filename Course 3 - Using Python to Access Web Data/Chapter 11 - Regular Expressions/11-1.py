import re
name = input("File name:")
if len(name) < 1:
    name = 'regex_sum.txt'
handle = open(name)
lst = list()
for line in handle:
    y = re.findall('([0-9]+)', line)
    if len(y) < 1: continue
    else:
        for x in y:
            lst.append(int(x))
print(sum(lst))
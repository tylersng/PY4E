name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
cts = dict()
for line in handle:
    if 'From ' in line:
        x = line.split()
        cts[(x[5].split(":"))[0]] = cts.get((x[5].split(":"))[0],0) + 1
[print(k, v) for k, v in sorted(cts.items())]

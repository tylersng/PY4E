name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    x = line.split()
    if 'From' not in x: continue
    else:
        counts[x[1]] = counts.get(x[1],0) + 1

bname = None
bcount = None
for name,count in counts.items():
    if bname is None or count > bcount:
        bname = name
        bcount = count

print(bname,bcount)

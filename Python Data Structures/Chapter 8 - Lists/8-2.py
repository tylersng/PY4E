fname = input("Enter file name: ") + ".txt"
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh :
    x = line.split()
    if 'From' not in x : continue
    elif len(line) < 3 : continue
    else :
        print(x[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
fname  = ("Enter file name: ") + ".txt"
fh = open(fname)
for line in fh:
    print(line.upper().rstrip())
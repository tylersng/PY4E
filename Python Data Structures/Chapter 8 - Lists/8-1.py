fname = input("Enter file name: ") + ".txt"
fh = open(fname)
lst = list()
ul = []
for line in fh:
    x = line.split()
    for word in x:
        if word in ul: continue 
        else : 
            ul.append(word)
ul.sort()
print(ul)
fname = input("enter file name:") + ".txt"
fh = open(fname)
count = 0
s = 0
print(len(fh.read()))
fh.seek(0)
for line in fh:
    count = count + 1
    print("Line Number:",count)
    print("Number of Letters: ",len(line))
    s = s + int(len(line))
print("\nProcess Done.\nTotal Lines:",count,"\nTotal Letters:",s)
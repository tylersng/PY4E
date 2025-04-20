fname = input("Enter file name: ") + ".txt"
count = 0
s = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    fline = line
    number_str = fline[fline.find(':') + 1:].strip()
    count = count + 1
    s = s + float(number_str)
print("Average spam confidence:",(s/count))

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
times = dict()
for line in handle: 
    if 'From ' in line:
        x = line.split()
        hr = x[5].split(":")
        times[hr[0]] = times.get(hr[0],0) + 1
    else: continue 
hrs = list()
for k,v in times.items():
    newtup = (k,v)
    hrs.append(newtup)

hrs = sorted(hrs)
for k,v in hrs:
    print(k,v)
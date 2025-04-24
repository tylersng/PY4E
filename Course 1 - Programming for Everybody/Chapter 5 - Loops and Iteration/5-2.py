largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try: 
        inum = int(num)
    except:
        print("Invalid input")
        continue
    # if largest or smallest is None - This is wrong cause or acts an operator and if largest is any value it will be true
    if largest is None or smallest is None :
        largest = inum
        smallest = inum
    elif inum > largest :
        largest = inum
    elif inum < smallest :
        smallest = inum

print("Maximum is", largest)
print("Minimum is", smallest)
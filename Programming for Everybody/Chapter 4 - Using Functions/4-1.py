def computepay(h, r):
    if h > 40: 
        return ((r*40)+((h-40)*(r*1.5)))
    else:
        return h * r

hrs = input("Enter Hours:")
rs = input("Enter Rates:")
try : 
    h = float(hrs)
    r = float(rs)
except:
    print("Please input a float")
    quit()
p = computepay(h, r)
print("Pay", p)
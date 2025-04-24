hrs = input("Enter Hours:")
rt = input("Enter Rates:")
try:    
    h = float(hrs)
    r = float(rt)
except:
    print("Error, please enter numeric input")
    quit()

if (h <= 40):
    pay = h * r
else :
    pay = (40 * r) + ((h-40)*(r*1.5))
print("Pay: ",pay)
hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter Rates:")
r = float(rt)
if (h <= 40.0):
    pay = h * r
else :
    pay = (40 * r) + ((h-40)*(r*1.5))
print(pay)
num = 0
tot = 0.0
while True: 
    x = input('Enter a number: ')
    if x == 'done' :
        break
    try :
        fx = float(x)
    except: 
        print('Invalid Input')
        continue 
    # print(fx)
    num = num + 1
    tot = tot + fx

# print('All done')
print(tot,num,tot/num)
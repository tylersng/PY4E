# for when recursion is more than 1000 in python max recursive error

import time
s_time = time.time()
def bup_fib(n): 
    if n == 1 or n == 2:
        return 1
    b_up = [0] * (n+1)
    b_up[1] = 1
    b_up[2] = 1
    for i in range(3,n+1):
        b_up[i] = b_up[i-1] + b_up[i-2]
    return b_up[n]

n = 1000
print(bup_fib(1000))
e_time = time.time()
x_time = e_time - s_time
print(f"Execution time: {x_time}.4f seconds")
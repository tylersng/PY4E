import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
print( sum( [int(x) for x in re.findall('[0-9]+',open("regex_sum.txt").read()) ] ) )
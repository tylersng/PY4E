import re
fruits = list()
fruits.append("apple")
fruits.append("banana")
fruits.append("peach")
fruits.append("kiwi")
fruits.append("lychee")
newfruits = [fruit for fruit in fruits if re.search('[a]+',fruit)]
print(newfruits)

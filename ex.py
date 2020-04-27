#!/usr/bin/python3
mydict={'val3':23,'val2':20,'val4':123,'val1':75}

print("\nBy Value")
for mykey,myvalue in sorted(mydict.items(), key=lambda x: x[1]):
    print("%s: %s"%(mykey,myvalue))


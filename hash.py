import hashlib

mystring = "This is a string"

print(hashlib.md5(mystring.encode()).hexdigest())
print(hashlib.sha1(mystring.encode()).hexdigest())
print(hashlib.sha256(mystring.encode()).hexdigest())

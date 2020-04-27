x = int(input("Pleae enter the beginning of the integer range> "))
y = int(input("Please enter the end of the integeer range> "))
for m in range(x,y):
    for n in range(2, m):
        if m % n == 0:
            print(m, "equals", n, "*", m//n)
            break
    else:
        print(m, "Is a prime number")
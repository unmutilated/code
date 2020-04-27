#!/usr/bin/python3
output = input("Would you like to output in: \n 1)binary \n 2)octal \n 3)hex \n 4)any base \n enter output number: ")
if output == "1":
    def output(binary):
        base = int(input("Please enter a base for conversion: "))
        baselib = {1:2, 2:4, 3:8, 4:16, 5:32, 6:64, 7:128, 8:256, 9:512, 10:1024, 11:2048, 12:4096, 13:8192, 14:16384 , 15:32768}
            #dictionary of base and what that means i.e... octal 8 has maximum of 256 values or 255 bits
        number = ""
        while(not(number.isnumeric())):
            number = input("What is the decimal to convert?: ")
        tempnumb = int(number)
        bin_output = ""
        while(0 < tempnumb < baselib[base]):
            bin_output = str(tempnumb % 2) + bin_output
                #divided by base with or without (remainder + itself)
            tempnumb = int(tempnumb / 2)
                #takes number entered and divided by base then directs up back to while statement
        print(bin_output)
    output("binary")

elif output == "2":
    def output(octal):
        number = ""
        while(not(number.isnumeric())):
            number = input("What is the decimal to convert?: ")
        tempnumb = int(number)
        bin_output = ""
        while(tempnumb > 0):
            bin_output = str(tempnumb % 8) + bin_output
                #similar to step 1 but base number has changed from 2 to 8
            tempnumb = int(tempnumb / 8)
        print(bin_output)
    output("octal")

elif output == "3":
    def output(hex):
        result = int(input("Enter a number to be converted to hexadecimal: "))
        hexadecimal = ""
        while result != 0:
            remainder = changeDigit(result % 16)
            hexadecimal = str(remainder) + hexadecimal
            result = int(result / 16)
        print(hexadecimal)
    def changeDigit(digit):
        decimal = [10, 11, 12, 13, 14, 15] # like step 1 with the dictionary were using 2 lists that correlate through the counter function
        hexadecimal = ["A", "B", "C", "D", "E", "F"]
        for counter in range(7):# its 7 not 6 because the [0,6] is 7
            if digit == decimal[counter - 1]: #-1 because base is 16 or 6 after 10: counts down to final output
                digit = hexadecimal[counter - 1]# same as above
        return digit
    output("hex")

elif output == "4":
    def output(allbase):# much like the binary step 1 and base for anything non alphanumeric
        base = int(input("Please enter a base for conversion: "))
        baselib = {1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512, 10: 1024, 11: 2048, 12: 4096,
                   13: 8192, 14: 16384, 15: 32768}
        alphanumeric = ""
        number = ""
        if base <= 15:
            while (not (number.isnumeric())):
                number = input("What is the decimal to convert?: ")
            tempnumb = int(number)
            bin_output = ""
            while (0 < tempnumb < baselib[base]):
                bin_output = str(tempnumb % base) + bin_output
                tempnumb = int(tempnumb / base)
            print(bin_output)
        elif base > 15:
            num = int(input("Please enter a number for conversion: "))
            while num != 0:
                remainder = changeDigit(num % base)# uses a scalable base formula
                alphanumeric = str(remainder) + alphanumeric
                num = int(num / base)
        print(alphanumeric)
    def changeDigit(digit): # much like step 3 but expands to over base 16 to base 36
        decimal = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        alphanumeric = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                         "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for counter in range(27):
            if digit == decimal[counter - 1]:
                digit = alphanumeric[counter - 1]
        return digit
    output("allbase")

else:
    print("There was an error or something")









def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def reverseNum(number):
    temp = str(number)
    temp = temp[::-1]
    return int(temp)

number = int(input("Enter a 4 digit number: "))
if (number>=1000 or number <=9999):
    sum = sum_of_digits(number)
    reversednum = reverseNum(number)
    print("Sum of digits is: ", sum)
    print("Reverse of the number is: ", reversednum)
else:
    print("invalid input")
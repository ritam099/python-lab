#for the star pattern 

num = int(input("Enter the number of the line wanted: "))
for i in range(1, num+1):
    print("*"*i)


#for the alphabet pyramid

import math
num = int(input("enter number of lines wanted : "))
space = num-1
for i in range(65,num+65):
    print(" "*space, end = "")
    for j in range (65,i+1):
        print(chr(j)," ", end = "")
    
    print()
    space-=1
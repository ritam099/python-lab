#Declaring the python list
firstList=[1001, 659, 75411, 654, 6125, 996]
print("Original List:", firstList)


#Sum of the items in the list
def sum_function(numbers):
    return sum(numbers)

final_sum = sum_function(firstList)
print("The sum of all the items in the List:", final_sum)


#multiplying all the items in list
def prod_function(numbers):
    product  = 1
    for number in numbers:
        product *= number
    return product

final_product= prod_function(firstList)
print("The product of the items in the list is:", final_product)


#get the largest number from a list
def find_largest(numbers):
    largest  = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

largest_number = find_largest(firstList)
print("The largest number in the list is:", largest_number)



#get the smallest number from a list.
def find_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


smallest_number = find_smallest(firstList)
print("The largest number in the list is:", smallest_number)
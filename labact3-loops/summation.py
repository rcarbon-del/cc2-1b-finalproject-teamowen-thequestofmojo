# Summation

# Variables & Input
input_number = int(input("Input: "))
sum = 0
formula_list = []

# Functions
# Formula
while len(formula_list) < input_number:
    for i in range(1, input_number+1):
        formula_list.append(i) # add the numbers to the list
print("Formula:", "+".join(map(str, formula_list))) # make the formula list into a string and join them with a plus sign

# Summation
for i in range(1, input_number+1): # loop the numbers from 1 to the input number
    sum += i # add the numbers to the sum
print("Summation:", sum)
# End of program


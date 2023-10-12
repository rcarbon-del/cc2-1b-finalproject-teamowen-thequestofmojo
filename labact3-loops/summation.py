# Summation

# Variables & Input
input_number = int(input("Input: "))
sum = 0
formula_list = []

# Functions
# Formula
while len(formula_list) < input_number:
    for i in range(1, input_number+1):
        formula_list.append(i)
print("Formula:", "+".join(map(str, formula_list)))

# Summation
for i in range(1, input_number+1):
    sum += i
print("Summation:", sum)
# End of program


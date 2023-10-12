# Summation

# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
input_number = int(input("Input: "))
sum = 0
print("Formula: ")
for i in range(1, input_number+1):
    print(i, end="+")

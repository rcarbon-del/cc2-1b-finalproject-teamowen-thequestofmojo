
fib = [1, 2]
counter = 1
fib_sum = fib[0] + fib[1]


while fib_sum < 40000000:
    fib.append(fib_sum)
    fib_sum = fib[counter] + fib[counter+1]
    counter += 1
print(fib)

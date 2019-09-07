#!/usr/bin/python3
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print (3 * number + 1)
        return 3 * number + 1

print('Enter an integer on which to run the Collatz Sequence:')

try:
    result = collatz(int(input()))
    while result != 1:
        result = collatz(result)

except ValueError:
    print('Please enter an integer!')

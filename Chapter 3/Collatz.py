import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    input = int(input())
except ValueError:
    print("Please enter a valid integer.")
    sys.exit()

while(input > 1):
    input = collatz(input)
    print(input)
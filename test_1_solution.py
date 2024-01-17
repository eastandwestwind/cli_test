import sys

# total arguments
n = len(sys.argv)

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

# Addition of numbers
Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])

print("\nSum of numbers:", Sum)
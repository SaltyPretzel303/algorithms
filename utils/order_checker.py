import sys
from input_reader import get_input

input = get_input()
if input == None:
    print("Please provide some input (piped data or path to the file) ... ")
    print("Exiting ... ")

    exit(1)

# assume that all values from input file are >=0
# in that case -1 is the lowest possible value
prev_val = -1
line = input.readline()

index = 0

while line:
    current_val = int(line)
    if current_val < prev_val:
        print(f"Input is not in correct (ascending) order at: {index}")
        print(f"Previous:{prev_val} Current:{current_val}")

        exit(1)

    prev_val = current_val
    index += 1

    line = input.readline()

input.close()

print("Input is in correct (ascending) order ... ")
exit(0)

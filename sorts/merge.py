from importlib.resources import open_text
import os
import sys
from typing import Dict
from utils.arg_parser import parse_input

INPUT_ARG = "in"
OUTPUT_ARG = "out"

args: Dict[str, str] = parse_input(sys.argv[1:], [INPUT_ARG, OUTPUT_ARG])

DEFAULT_OUTPUT = "./output"

if args == None or args == {} or INPUT_ARG not in args:
    print("Please provide input and output file arguments:")
    print("Input file as: \t--in")
    print("Output file as: \t--out ")

    exit(1)

if not os.path.exists(args.get(INPUT_ARG)):
    print("Provided input file does not exists ... ")

    exit(1)


input = open(args.get(INPUT_ARG), "r")
lines = input.readlines()
input.close()

values = []
for line in lines:
    values.append(int(line))

print(f"Read: {len(values)} values ...")
print("Ready to sort them ...")


def merge_sort(data, start_ind: int, end_ind: int):

    if(start_ind < end_ind):
        mid_ind = int(start_ind + (end_ind - start_ind)/2)

        merge_sort(data, start_ind, mid_ind)
        merge_sort(data, mid_ind+1, end_ind)

        merge(data, start_ind, mid_ind, end_ind)


def merge(data, start_ind, mid_ind, end_ind):

    left_part = data[start_ind: mid_ind+1]
    left_ind: int = 0
    left_count = len(left_part)

    right_part = data[mid_ind+1:end_ind+1]
    right_ind: int = 0
    right_count = len(right_part)

    out_indices = list(range(start_ind, mid_ind)) + \
        list(range(mid_ind, end_ind+1))

    for out_ind in out_indices:
        if(left_ind < left_count and right_ind < right_count):
            if(left_part[left_ind] > right_part[right_ind]):
                data[out_ind] = right_part[right_ind]
                right_ind += 1
            else:
                data[out_ind] = left_part[left_ind]
                left_ind += 1
        else:
            if(left_ind == left_count):
                data[out_ind] = right_part[right_ind]
                right_ind += 1
            else:
                data[out_ind] = left_part[left_ind]
                left_ind += 1


merge_sort(values, 0, len(values)-1)

print("Sorting done ... ")

output_path = DEFAULT_OUTPUT
if OUTPUT_ARG in args:
    output_path = args.get(OUTPUT_ARG)

print(f"Writing data to {output_path}")

f = open(output_path, "w")
for v in values:
    f.write(str(v)+'\n')
    # by writing them this way every line will contain only single value
f.close()

print("Writing done ... exiting ... ")

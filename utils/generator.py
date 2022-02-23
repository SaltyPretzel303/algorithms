import random
import sys
from typing import Dict
from arg_parser import parse_input

MIN_ARG = "min"
MAX_ARG = "max"
COUNT_ARG = "count"

args: Dict[str, str] = parse_input(sys.argv[1:], [MIN_ARG, MAX_ARG, COUNT_ARG])
if args == None or args == {}:
    print("Please provide arguments for: ")
    print("Minimum value as: \t--min")
    print("Maximum value as: \t--max")
    print("Values count as: \t--count")

    exit(1)

DEFAULT_COUNT = 200
DEFAULT_MIN_VALUE = 0
DEFAULT_MAX_VALUE = sys.maxsize

count = DEFAULT_COUNT
min = DEFAULT_MIN_VALUE
max = DEFAULT_MAX_VALUE


if MIN_ARG in args:
    min = int(args.get(MIN_ARG))

if MAX_ARG in args:
    max = int(args.get(MAX_ARG))

if COUNT_ARG in args:
    count = int(args.get(COUNT_ARG))

print(f"Generating: {count} values between {min} and {max} ... ")

values = list(range(min, max))
random.shuffle(values)
values = values[0:count]

for v in values:
    print(v)

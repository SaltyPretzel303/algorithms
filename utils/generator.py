import os
import random
import sys
from typing import Dict
from arg_parser import parse_input

# Next arguments can be provided:
#     - minimum value as: --min;    default:   0
#     - maximum value as: --max;    default:   sys.maxsize (int.max)
#     - values coutn as:  --count;  default:   200
#     - output path as:   --out;    default:   console stdout

MIN_ARG = "min"
MAX_ARG = "max"
COUNT_ARG = "count"
OUT_ARG = "out"

DEFAULT_COUNT = 200
DEFAULT_MIN_VALUE = 0
DEFAULT_MAX_VALUE = sys.maxsize
DEFAULT_OUTPUT_STREAM = sys.stdout

args: Dict[str, str] = parse_input(
    sys.argv[1:],
    [MIN_ARG, MAX_ARG, COUNT_ARG, OUT_ARG])

count = DEFAULT_COUNT if COUNT_ARG not in args else int(args.get(COUNT_ARG))
min = DEFAULT_MIN_VALUE if MIN_ARG not in args else int(args.get(MIN_ARG))
max = DEFAULT_MAX_VALUE if MAX_ARG not in args else int(args.get(MAX_ARG))
out_path = None if OUT_ARG not in args else args.get(OUT_ARG)

file_stream = None
if OUT_ARG in args and os.path.exists(args.get(OUT_ARG)):
    file_stream = open(args.get(OUT_ARG), "w")

out_stream = file_stream if file_stream != None else DEFAULT_OUTPUT_STREAM

index = 0
while index < count:
    # values.append(random.randint(min, max))
    out_stream.write(str(random.randint(min, max))+"\n")
    index += 1

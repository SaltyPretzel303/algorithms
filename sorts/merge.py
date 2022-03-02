from utils.logs_holder import LogsHolder
from utils.stopwatch import Stopwatch
from utils.input_reader import get_input

# First cli argument (if provided) will be the path to the file with unsorted values
# If file path is not provided sys.stdin will be read (piped values)

# logs will be stored in $DEFAULT_LOG_PATH

DEFAULT_LOG_PATH = "./logs"

logs = LogsHolder()

input_stream = get_input()

if input_stream == None:
    print("Input stream is empty (no piped data) and the file path is not provided ... ")
    print("Exiting ... ")

    exit(1)

stopwatch = Stopwatch()

stopwatch.start()

values = input_stream.readlines()
input_stream.close()

for i in range(0, len(values)):
    values[i] = int(values[i])

stopwatch.stop()

logs.add_log(f"Read {len(values)} values in: {stopwatch.get_time_str()}... ")


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


stopwatch.start()
merge_sort(values, 0, len(values)-1)
stopwatch.stop()

logs.add_log(f"Sorting time: {stopwatch.get_time_str()}")

stopwatch.start()

for v in values:
    print(v)

stopwatch.stop()

logs.add_log(f"Printing time: {stopwatch.get_time_str()}")

logs.write(DEFAULT_LOG_PATH)

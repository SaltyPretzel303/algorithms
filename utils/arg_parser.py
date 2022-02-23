import getopt
from typing import Dict


# returns dictionary of string key/value pairs parsed from 'provided_argv'
# all keys are equal to items from 'required' list

# in case of an error it will be printed and None will be returned

# method will parse only long arguments (ones that are specified with -- in front)
# e.g. --min 10 --max 20
# will return {"min":"10","max":20}


def parse_input(provided_argv: list(), required: list()) -> Dict[str, str]:
    if provided_argv == None or len(provided_argv) < 2:
        return None

    args = format_as_args(required)

    try:

        parsed, left_args = getopt.getopt(provided_argv, "", args)

        map = convert_to_map(parsed)

        return map

    except getopt.GetoptError as err:
        print(err)
        return None


# transform args to format required by 'getopt'
def format_as_args(input):

    args = []

    for item in input:
        args_item = item+"="
        args.append(args_item)

    return args


def convert_to_map(input):
    map = {}
    for key, value in input:
        new_key = key.replace('-', '')
        map[new_key] = value

    return map

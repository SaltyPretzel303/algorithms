import os
import sys
from typing import TextIO

# if some input is piped to this command it will be stored in sys.stdin (and returned)
# otherwise first cli argument is gonna be used as path to the file for which
# TextIO will be returned
# if none of these above is provided None is returned

# don't forget to close this TextIO after the data processing is done


def get_input() -> TextIO:

    input_stream = None

    # use stdin if it's full
    if not sys.stdin.isatty():
        input_stream = sys.stdin

        # sys.stdin.isatty()
        # Return True if the file descriptor fd is open and connected
        # to a tty(-like) device, else False.

    # otherwise, read the given filename
    else:
        try:
            input_filename = sys.argv[1]

            if os.path.exists(input_filename):
                input_stream = open(input_filename, 'r')

        except IndexError:
            # will happen if cli argument is not provided
            message = 'Filename required as first argument if stdin is not full'
            print(message)

    return input_stream

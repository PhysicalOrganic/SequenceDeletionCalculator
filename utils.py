# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# This software is licensed under the MIT License.
# See the LICENSE file for more information.

'''
Contains miscellaneous utilities
'''

class SequenceError(Exception):
    '''Generic sequence error'''


def print_progress_bar(iteration: int,
                       total: int,
                       decimals=1,
                       bar_len=25,
                       fill='🚀',
                       print_ending: str = '\r'):
    '''
    Prints a progress bar of a loop if called within that loop.

    Parameters
    ----------
    iteration : int
        Current interation value

    total : int
        Total number of iterations

    decimals : int
        Number of decimal points to display

    bar_len : int
        Length of the progress bar in the terminal

    fill_char : str
        Character used to fill the progress bar

    print_ending : str
        Character to terminate the progress bar

    Returns
    -------
    None
    '''
    if total == 0:
        pass
    else:
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_len = int(bar_len * iteration // total)
        prog_bar = fill * filled_len + '-' * (bar_len - filled_len)
        print(f'\r\r|{prog_bar}| {percent}%', end=print_ending)

        # Print New Line on Complete
        if iteration == total:
            print("\n")

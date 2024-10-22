# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# This software is licensed under the MIT License.
# See the LICENSE file for more information.

'''
Generates the possible sequences that result
from the deletion of monomers from a sequence
defined oligourethane
'''

import itertools
import argparse

from time import time
from pathlib import Path

from collections import Counter
from typing import List

from adducts import ADDUCTS
from monomers import ONE_LETTER_CODE_MASS_PAIRS, THREE_LETTER_CODES
from utils import SequenceError, print_progress_bar


__author__ = "James Howard"
__copyright__ = "2024, James R. Howard"
__credits__ = ["James R. Howard", "Christopher Wight"]
__license__ = "MIT"
__version__ = "2.1.1"
__maintainer__ = "James Howard"
__email__ = "jrhoward@utexas.edu"
__status__ = "Production"


DESCRIPTION = '''
              Generates the possible sequences that result
              from the deletion of monomers from a sequence
              defined oligourethane
              '''


def get_args():
    '''
    Parses CLI arguments
    '''
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument('-i',
                        '--input',
                        metavar='\b',
                        help='Input sequence of 1-letter codes',
                        action='store',
                        required=True,
                        dest='input_sequence')

    parser.add_argument('-d',
                        '--decimal',
                        metavar='\b',
                        help='Number of decimal points to use',
                        action='store',
                        required=False,
                        type=float,
                        default=3,
                        dest='decimal_points')

    args = parser.parse_args()

    return args


def convert_to_one_letter_codes(input_list: list[str]) -> str:
    '''
    Converts 3-letter codes to their corresponding 1-letter monomer codes.

    Parameters
    ----------
    input_list : list[str]
        List of strings representing monomer codes, which may be
        1-letter codes or longer (3-letter) codes.

    Returns
    -------
    str
        String of 1-letter monomer codes

    Raises
    ------
    SequenceError
        If a monomer in input_list cannot be converted
    '''
    input_string = ''

    for monomer in input_list:

        if len(monomer) == 1:

            input_string = input_string + monomer

        elif monomer in THREE_LETTER_CODES:

            input_string = input_string + THREE_LETTER_CODES[monomer]

        # Check if monomer is not in the definitions
        elif monomer not in THREE_LETTER_CODES:

            # If all the letters of a monomer are in the unique
            # letter codes append that to the final string
            if all([x in ONE_LETTER_CODE_MASS_PAIRS for x in monomer]):

                input_string = input_string + monomer

        else:
            raise SequenceError('Input sequence not understood')

    return input_string


def parse_input(input_sequence: str) -> str:
    '''
    Parses user input and converts it into a string of 1-letter monomer codes.

    Parameters
    ----------
    input_sequence : str
        String representing the user input, which may be
        1-letter codes or longer (3-letter) codes.

    Returns
    -------
    str
        String of 1-letter monomer codes
    '''
    input_list = list(input_sequence.split())

    if all([len(monomer) == 1 for monomer in input_list]):
        return ''.join(input_list)
    else:
        return convert_to_one_letter_codes(input_list)


def verify_sequence(input_string) -> None:
    '''

    Parameters
    ----------
    input_string : String
        String of urethane monomer 1-letter codes i.e. 'ACCABD'
        where each letter corresponds to a monomer

    Raises
    ------
    SequenceError
        Invalid sequence
    '''
    for monomer in input_string:
        if monomer not in ONE_LETTER_CODE_MASS_PAIRS:
            raise SequenceError(f'{monomer} monomer not in possible monomers')
    return True


def generate_deletion_possibilities(sequence: str) -> list[str]:
    '''
    Generates a list of possible deletions of a sequence
    of 1-letter codes.

    Example
    -------
    For the input sequence 'AyB', the function will return:
    ['', 'A', 'y', 'B', 'Ay', 'AB', 'yB', 'AyB']

    Parameters
    ----------
    sequence : str
        String of urethane monomer 1-letter codes i.e. 'ACCABD'
        where each letter corresponds to a monomer

    Returns
    -------
    list[str]
        A list of all possible deletions (subsequences) of the input sequence.
    '''
    print('Generating possible deletions\n')

    # Start the progress bar
    total_len = len(sequence)
    print_progress_bar(0, total=total_len, bar_len=10)

    possibilities = []
    for monomer in range(total_len + 1):
        for combination in itertools.combinations(sequence, monomer):
            if combination not in possibilities:

                # Converts the list of tuples to a list of strings
                possibilities.append(''.join([c for c in combination]))
        print_progress_bar(monomer, total_len)

    return possibilities


def get_mass(sequence) -> float:
    '''
    Calculates the total mass of a sequence of monomer 1-letter codes.

    This function iterates through a sequence and sums the masses of
    each monomer based on the 1-letter code:mass pairs.

    Parameters
    ----------
    sequence : str
        String of urethane monomer 1-letter codes i.e. 'ACCABD'
        where each letter corresponds to a monomer

    Returns
    -------
    float
        The total mass of the sequence.
    '''
    # Starting mass of 0
    mass = 0
    for m in sequence:
        mass += ONE_LETTER_CODE_MASS_PAIRS[m]
    return float(mass)


def is_permutation(sequence1, sequence2) -> bool:
    '''
    Determines if a string is a permutation of another string

    Returns
    -------
    bool
        True if the sequences are permutations of eachother
    '''
    if sorted(sequence1) == sorted(sequence2):
        return True
    else:
        return False


def find_missing(sequence: str, target: str):
    '''
    Identifies monomers present in the target sequence that are missing from the provided sequence.

    Parameters
    ----------
    sequence : str
        String of urethane monomer 1-letter codes i.e. 'ACCABD'
        where each letter corresponds to a monomer. This sequence
        is compared against the target sequence.

    target : str
        String of urethane monomer 1-letter codes i.e. 'ACCABD'
        where each letter corresponds to a monomer. This sequence
        is used as the 'correct' sequence and should contain more
        monomers than the sequence.

    Returns
    -------
    dict
        A dictionary where the keys are 1-letter codes that are
        missing from the sequence, and the values are the counts
        of each missing monomer in the target sequence.
    '''
    missing = dict(Counter(target) - Counter(sequence))
    return missing


def filter_identical_sequences(possibilities, verbose=False) -> List[str]:
    '''
    Parameters
    ----------
    possibilities : list
        list of tuples which represent oligomers in their
        1-letter code format

    Returns
    -------
    possibilities : list
        list of tuples which represent oligomers in their
        1-letter code format, removed of permutations
    '''
    # Determine max sequence size
    max_length = len(max(possibilities, key=len)) + 1

    if verbose:
        print(f"Max sequence length: {max_length}")

    print('Assessing deletion similarity\n')
    print_progress_bar(0, max_length, bar_len=10)

    unique = []

    for size in range(max_length):

        # Separate list of possibilities into their respective sizes
        contending_sequences = [x for x in possibilities if len(x) == size]

        for s in contending_sequences:
            if sorted(s) not in unique:
                unique.append(sorted(s))

        print_progress_bar(size + 1, max_length)

    return unique


def write_adducts(input_sequence: str,
                  deletions: dict,
                  decimal_points: int,
                  outfile: Path) -> None:
    '''
    Writes the details of the deletions and their adducts to an output file.

    Parameters
    ----------
    input_sequence : str
        String of urethane monomer 1-letter codes i.e. 'ACCABD'
        where each letter corresponds to a monomer

    deletions : dict
        A dictionary where keys are deletion sequences (strings) and values are
        additional information relevant to each deletion.

    decimal_points : int
        The number of decimal points to which the masses will be rounded.

    outfile : Path
        The path to the output file.
    '''

    print('Writing to file\n')

    # Make progress bar
    total_len = len(deletions)
    print_progress_bar(0, total_len, bar_len=10)

    with open(outfile, 'w', encoding='utf-8') as o:

        for i, deletion in enumerate(deletions):
            base_mass = get_mass(deletion)

            # Write the mass of the parent deletion
            o.write(f'{"".join([letter + " " for letter in deletion])} :  \
                      {round(base_mass, decimal_points)}\n')

            # Missing monomer information
            missing = find_missing(deletion, input_sequence)
            o.write("Missing ")
            for missing_monomer, occurences in missing.items():
                o.write(f'{occurences} {convert_to_multiletter_codes(missing_monomer)} ')

            o.write("\n")
            o.write('CHARGE\tTERMINUS\tNAME\t\tM/Z\n')
            for adduct in ADDUCTS:
                chrg = int(adduct.charge)
                terminus = adduct.terminus
                name = f'{adduct.name:<16}'
                m_over_z = abs(round((base_mass + adduct.mass) / chrg, decimal_points))
                o.write(f'{chrg}\t{terminus}\t{name}\t{m_over_z}\n')

            o.write("\n")
            print_progress_bar(i + 1, total_len)


def convert_to_multiletter_codes(monomer_one_letter):
    '''
    Converts a 1-letter monomer code to its corresponding 3-letter code.

    This function looks up the provided 1-letter code in a predefined dictionary
    of three-letter codes and returns the corresponding 3-letter code.

    Parameters
    ----------
    monomer_one_letter : str
        A single character of the 1-letter code

    Returns
    -------
    str
        The 3-letter code associated with the input 1-letter code

    '''
    return next(key for key, value in THREE_LETTER_CODES.items() if value == monomer_one_letter)


def main():
    '''
    Main function
    '''
    t1 = time()

    args = get_args()

    # How precise do you want to get?
    decimal_points = int(args.decimal_points)

    input_sequence = args.input_sequence

    # Parse input list to accomodate multiletter codes
    input_sequence = parse_input(args.input_sequence)

    # Check to ensure sequence is legal
    verify_sequence(input_sequence)

    possibilities = generate_deletion_possibilities(input_sequence)

    deletions = filter_identical_sequences(possibilities, verbose=False)

    write_adducts(input_sequence,
                  deletions,
                  outfile=Path().cwd() / f'{input_sequence}.txt',
                  decimal_points=decimal_points)

    t2 = time()

    print(f'Completed sequence deletion calculator in {round(t2 - t1, 2)} seconds')


if __name__ == "__main__":
    main()

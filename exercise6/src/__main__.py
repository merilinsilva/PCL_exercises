#### Imports#############################################
from src.levenshtein_cli import CustomizableLevenshteinCalculator
import argparse
import os
import sys
########################################################


def check_for_positive_and_valid_value(value: int | float) -> None:
    """
    This function checks if the value is higher or equal to zero and if it's an integer or floating point number and raises and error if not.

    Args:
        value (int | float): value, here the levenstein operation costs
    """
    try:
        value = float(value)
        if value < 0.0:
            # The argparse Type Error object was used to give meaningful messages, if the costs aren't positive or 0
            raise argparse.ArgumentTypeError(
                "The levenstein operation costs must be zero or higher")
    except ValueError:
        raise argparse.ArgumentTypeError(
            "The levenstein operation costs must be an integer or floating point number")


def main():
    # The ArgumentParser object is defined, which includes the programs name, the description and also a option to exit the parser if an error occurs
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]), exit_on_error=True, description='This program has a class that creates CLI with a argparse to calculate the levenstein distance between two words', add_help=True, allow_abbrev=True)

    # All the required arguments are added and the types of the arguments are defined.
    # Required arguments are saved as such
    parser.add_argument(
        '-f1', '--file1', type=str, help='Absolute path to the first/ source file', required=True)
    parser.add_argument(
        '-f2', '--file2', type=str, help='Absolute path to the second/ target file', required=True)
    parser.add_argument(
        '-i', '--insertion', default=1, help='Enter the desired weight of an insertion operation')
    parser.add_argument(
        '-d', '--deletion', default=1, help='Enter the desired weight of a deletion operation')
    parser.add_argument(
        '-s', '--substitution', default=1, help='Enter the desired weight of a substitution operation')
    parser.add_argument('-t', '--tokenize', action='store_true',
                        default=False, help='Use if tokenization is wished to be done on token-level')
    args = parser.parse_args()

    # Check if all the costs are zero or higher and if they are an integer or floating point number
    # I did try to add multiple type options in the add_argument yet that doesn't seem to be possible (only one type definable) thus I had to check in a separate function
    check_for_positive_and_valid_value(args.insertion)
    check_for_positive_and_valid_value(args.deletion)
    check_for_positive_and_valid_value(args.substitution)

    # Use the defined class to calculate the optimal levenstein difference cost
    distances = CustomizableLevenshteinCalculator(args.file1, args.file2, args.insertion,
                                                  args.deletion, args.substitution, args.tokenize).levenstein_calculation()
    # All lines are separately printed
    for distance in distances:
        print(distance)


if __name__ == '__main__':
    main()

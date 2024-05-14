############ Imports#####################
from src.levenshtein_base import levenshtein
from string import punctuation
from typing import Self
#########################################

# Student Name: Merilin Sousa Silva
# Matriculation Number: 23-726-086


class CustomizableLevenshteinCalculator():
    """
    This class parses the file contents and performs a levenshtein distance calculation on token or character level

    Args:
        file1_path(str): file path to the first file
        file2_path(str): file path to the second file
        insertion_cost(int | float): cost of insertion
        deletion_cost(int | float): cost of deletion
        substitution_cost(int | float): cost of substitution
        tokenize_value(bool): if True then the levenshtein distance is calculated on token-level, else on character-level
    """

    def __init__(self, file1_path: str, file2_path: str, insertion_cost: int | float, deletion_cost: int | float, substitution_cost: int | float, tokenize_value: bool) -> None:
        """
        Initializes the attributes after the a class object is constructed

        Args:
            file1_path (str): file path to the first file
            file2_path (str): file path to the second file
            insertion_cost (int | float): cost of insertion
            deletion_cost (int | float): cost of deletion
            substitution_cost (int | float): cost of substitution
            tokenize_value (bool): if True then the levenshtein distance is calculated on token-level, else on character-level
        """
        self.file1_path = file1_path
        self.file2_path = file2_path
        self.insertion = float(insertion_cost)
        self.deletion = float(deletion_cost)
        self.substitution = float(substitution_cost)
        self.tokenize = tokenize_value

    @staticmethod
    def punctuation_removal(file: list[str]) -> list[str]:
        """
        Cleans the lines in the content list by removing all punctuation except for apostrophes in contractions.

        Args:
            file (list[str]): list of all lines of a file

        Returns:
            list[str]: list of all lines without punctuation of a file
        """
        clean_file = []

        # Iteration through the lines to remove punctuation signs
        for line in file:
            # Through the translate function a translation table is created where all punctuation, except for the apostrophe is removed from each line
            clean_line = line.translate(str.maketrans(
                "", "", punctuation.replace("'", "")))
            # The cleaned lines are appended to a new list that is finally returned
            clean_file.append(clean_line)

        return clean_file

    def levenstein_calculation(self: Self) -> list[float]:
        """
        Opens the two files, reads their contents and depending on if the levenshtein calculation is done on character or token-level the lines will be preprocessed and split.

        Args:
            self (Self): Instance attribute of the class object

        Raises:
            ValueError: if the two file do not contain equal amounts of lines then a error message is raised with a meaningful message

        Returns:
            list[float]: a list of all levenshtein distances calculated on each line is returned
        """
        # Both files are opened for reading and the lines are saved in lists as variables
        # Error handling in the case of a file path being wrong
        try:
            with open(self.file1_path, 'r', encoding='utf-8') as file1:
                content_file1 = file1.readlines()

            with open(self.file2_path, 'r', encoding='utf-8') as file2:
                content_file2 = file2.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(
                'One or both of the file paths do not exist')
        # Make sure the encoding Error is catched and handled meaningfully
        except UnicodeError:
            raise UnicodeError(
                "Failed to read file with utf-8 encoding, please make sure the files have one of these encodings.")

            # Check for equal length of the two file contents and ValueError is raised if they aren't equally long
        if len(content_file1) != len(content_file2):
            raise ValueError(
                "the source and target file have to contain the same amount of lines")

        # If the levenshtein calculation happens on character-level then the levenshtein function can be automatically used
        if not self.tokenize:
            # distances = []
            # # On each line the levenshtein distance is calculated and appended to the distances list
            # for i in range(len(content_file1)):
            #     distances.append(levenshtein(content_file1[i], content_file2[i],
            #                                  self.insertion, self.deletion, self.substitution))
            distances = [levenshtein(content_file1[i], content_file2[i], self.insertion,
                                     self.deletion, self.substitution) for i in range(len(content_file1))]
            return distances
        # Otherwise punctuation needs to be removed prior to the calculation
        else:
            # distances = []
            # The predefined static method is used to remove punctuation from the file content lists
            clean_file1 = self.punctuation_removal(content_file1)
            clean_file2 = self.punctuation_removal(content_file2)
            # # Since the levenshtein calculation is done on token-leve, token lists have to be used as the file arguments (thus split() is used)
            # for i in range(len(clean_file1)):
            #     distances.append(levenshtein(clean_file1[i].split(), clean_file2[i].split(),
            #                                  self.insertion, self.deletion, self.substitution))
            distances = [levenshtein(clean_file1[i].split(), clean_file2[i].split(),
                                     self.insertion, self.deletion, self.substitution) for i in range(len(clean_file1))]
            return distances

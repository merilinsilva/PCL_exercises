from src.levenshtein_cli import CustomizableLevenshteinCalculator
import pytest


def test_unequal_lines():
    """
    Test if ValueError is raised if the length of the files is not equally long.
    """
    with pytest.raises(ValueError):
        class_obj = CustomizableLevenshteinCalculator(
            'samples/openAI_1.txt', 'samples/openAI_2.txt', 1, 1, 1, False)
        class_obj.levenstein_calculation()


def test_file_not_found():
    """
    Test if FileNotFoundError causes a meaningful error message to be printed if the file path doesn't exist.
    """
    with pytest.raises(FileNotFoundError):
        class_obj = CustomizableLevenshteinCalculator(
            'samples/openAI_4.txt', 'samples/openAI_2.txt', 1, 1, 1, False)
        class_obj.levenstein_calculation()


def test_encoding_error():
    """
    Test if UnicodeDecodeError causes a meaningful error message to be printed.
    """
    with pytest.raises(UnicodeError):
        class_obj = CustomizableLevenshteinCalculator(
            'samples/library_1.txt', 'samples/library_2_invalid_encoding.txt', 1, 1, 1, False)
        class_obj.levenstein_calculation()


def test_initialization():
    """
    Tests if the attributes are initialized correctly
    """
    class_obj = CustomizableLevenshteinCalculator(
        'samples/library_1.txt', 'samples/library_2.txt', 1, 1, 1, False)
    assert class_obj.file1_path == 'samples/library_1.txt'
    assert class_obj.file2_path == 'samples/library_2.txt'
    assert class_obj.insertion == 1
    assert class_obj.deletion == 1
    assert class_obj.substitution == 1
    assert class_obj.tokenize == False


def test_punctuation_removal():
    """
    Test if the punctuation removal function works
    """
    # Case with no punctuation
    input_list = ['hi my name is merilin']
    output_list = ['hi my name is merilin']
    assert CustomizableLevenshteinCalculator.punctuation_removal(
        input_list) == output_list

    # Case with punctuation
    input_list = ['hi? my name, is merilin.']
    output_list = ['hi my name is merilin']
    assert CustomizableLevenshteinCalculator.punctuation_removal(
        input_list) == output_list

    # Apostrophe case
    input_list = ["hi? my name, is merilin, it's."]
    output_list = ["hi my name is merilin it's"]
    assert CustomizableLevenshteinCalculator.punctuation_removal(
        input_list) == output_list


def test_levenstein_calculation():
    """
    Tests if the levenshtein distance is calculated correctly
    """
    # Character-level levenshtein calculation
    class_obj = CustomizableLevenshteinCalculator(
        'samples/library_1.txt', 'samples/library_2.txt', 1, 1, 1, False)
    assert class_obj.levenstein_calculation()[0] == 33.0

    # Token-level levenshtein calculation
    class_obj = CustomizableLevenshteinCalculator(
        'samples/library_1.txt', 'samples/library_2.txt', 1, 1, 1, True)
    assert class_obj.levenstein_calculation()[0] == 5.0

    # Character-level
    class_obj = CustomizableLevenshteinCalculator(
        'samples/file1.txt', 'samples/file2.txt', 1, 1, 1, False)
    assert class_obj.levenstein_calculation() == [2.0, 4.0]

    # Word level
    class_obj = CustomizableLevenshteinCalculator(
        'samples/file1.txt', 'samples/file2.txt', 1, 1, 1, True)
    assert class_obj.levenstein_calculation() == [2.0, 2.0]

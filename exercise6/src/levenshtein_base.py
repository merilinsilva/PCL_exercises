def levenshtein(file1: str | list[str], file2: str | list[str], insertion_cost: int, deletion_cost: int, substitution_cost: int) -> float:
    """
    This function calculates the levenstein distance of at character or token level and the weights of the operations are adjustable.

    Args:
        file1 (str | list[str]): if the file1 content is a string then the levenstein distance is calculated on character level otherwise it's calculated on token level
        file2 (str | list[str]): if the file2 content is a string then the levenstein distance is calculated on character level otherwise it's calculated on token level
        insertion_weight (int): This operation value is by default 1 but can be customized.
        deletion_weight (int): This operation value is by default 1 but can be customized.
        substitution_weight (int): This operation value is by default 1 but can be customized.

    Returns:
        float: The levenstein distance between the contents of the source file1 and the target file2
    """
    # The token or character length is calculated
    n, m = len(file1), len(file2)
    # Empty Matrix is created
    dp_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # The first row and column of the matrix
    # Base Case: Cost for inserting characters into an empty 'a' to match 'b'
    for j in range(m + 1):
        dp_matrix[0][j] = j
    # Base Case: Cost for deleting characters from 'a' to match an empty 'b'
    for i in range(n + 1):
        dp_matrix[i][0] = i

    # Transitions
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the last letter is the same
            if file1[i-1] == file2[j-1]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1]
            else:
                # From all prior fields the according operations are added and the smallest value is chosen and saved in the new current field
                dp_matrix[i][j] = min(
                    dp_matrix[i-1][j] + insertion_cost,  # Insertion
                    dp_matrix[i][j-1] + deletion_cost,  # Deletion
                    dp_matrix[i-1][j-1] + substitution_cost  # Substitution

                )

    # Return the final matrix element and thus the levenstein distance
    return dp_matrix[n][m]

import numpy as np


def sawnorm(matrix: np.ndarray, crit_type: list[str]) -> np.ndarray:
    """
    ### SAW Normalization
    Calculates the normalization matrix using the Simple Additive Weighting (SAW) method.

    This function takes a decision matrix and a list of criteria types,
    then generates a normalization matrix based on the SAW method.

    Args:
        matrix (np.ndarray): The decision matrix (NumPy array) with shape (number_of_alternatives, number_of_criteria).
            Each row represents an alternative, and each column represents a criterion.
            The values in the matrix must be numeric.
        crit_type (list[str]): A list containing the criteria type for each column in the decision matrix.
            Each element in the list must be a string, either 'benefit' or 'cost'.
            'benefit' indicates that the higher the value, the better.
            'cost' indicates that the lower the value, the better.
            The length of this list must be equal to the number of columns in the decision matrix.

    Returns:
        np.ndarray: The normalization matrix (NumPy array) with the same shape as the decision matrix.
            The values in this matrix are normalized based on the SAW method.

    Raises:
        ValueError: If the number of criteria types is not equal to the number of matrix columns.
        ValueError: If a criteria type is invalid (not 'benefit' or 'cost').

    Examples:
        >>> matrix = np.array([[8, 7, 9, 6], [7, 9, 8, 8], [9, 8, 6, 7]])
        >>> crit_type = ['benefit', 'cost', 'benefit', 'cost']
        >>> sawnorm(matrix, crit_type)
        array([[0.88888889, 0.77777778, 1.        , 0.75      ],
               [0.77777778, 1.        , 0.88888889, 1.        ],
               [1.        , 0.88888889, 0.66666667, 0.875     ]])
    """

    if len(crit_type) != matrix.shape[1]:
        raise ValueError(
            "The number of criteria types must be equal to the number of matrix columns."
        )

    norm_matrix = np.zeros_like(matrix, dtype=float)

    for j in range(matrix.shape[1]):
        if crit_type[j].lower() == "benefit":
            norm_matrix[:, j] = matrix[:, j] / np.max(matrix[:, j])
        elif crit_type[j].lower() == "cost":
            norm_matrix[:, j] = np.min(matrix[:, j]) / matrix[:, j]
        else:
            raise ValueError(
                f"Invalid criteria type: {crit_type[j]}. Must be 'benefit' or 'cost'."
            )

    return norm_matrix

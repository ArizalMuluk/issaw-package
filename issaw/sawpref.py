import numpy as np
from .sawnorm import sawnorm



def sawpref(norm_matrix: np.ndarray, weight: list[float]) -> np.ndarray:
    """
    ### SAW Preference
    Calculates the preference values using the Simple Additive Weighting (SAW) method.

    This function takes a normalization matrix and a list of weights,
    then generates the preference values based on the SAW method.

    Args:
        norm_matrix (np.ndarray): The normalization matrix (NumPy array) with shape (number_of_alternatives, number_of_criteria).
            Each row represents an alternative, and each column represents a criterion.
            The values in this matrix are already normalized.
        weight (list[float]): A list containing the weights for each criterion.
            Each element in the list must be a float.
            The length of this list must be equal to the number of columns in the normalization matrix.

    Returns:
        np.ndarray: An array containing the preference values for each alternative.

    Raises:
        ValueError: If the number of weights is not equal to the number of columns in the normalization matrix.

    Examples:
        >>> norm_matrix = np.array([[0.88888889, 0.77777778, 1.        , 0.75      ],
        ...                        [0.77777778, 1.        , 0.88888889, 1.        ],
        ...                        [1.        , 0.88888889, 0.66666667, 0.875     ]])
        >>> weight = [0.4, 0.3, 0.2, 0.1]
        >>> sawpref(norm_matrix, weight)
        array([0.85555556, 0.86666667, 0.86666667])
    """
    if len(weight) != norm_matrix.shape[1]:
        raise ValueError(
            "The number of weights must be equal to the number of columns in the normalization matrix."
        )

    return np.sum(norm_matrix * weight, axis=1)

import numpy as np


class SAW:
    """
    A class for performing Simple Additive Weighting (SAW) calculations.
    """

    def __init__(self, matrix, criteria, weight):
        """
        Initializes the SAW object with the decision matrix, criteria, and weights.

        Args:
            matrix (list or np.ndarray): The decision matrix. Can be a list of lists or a NumPy array.
            criteria (list[str]): A list of criteria types ('benefit' or 'cost').
            weights (list[float]): A list of weights for each criterion.
        """
        self.matrix = matrix
        self.criteria = criteria
        self.weight = weight

        if len(self.criteria) != len(self.weight):
            raise ValueError(
                "The number of criteria must be equal to the number of weights."
            )

        if len(self.weight) != self.matrix.shape[1]:
            raise ValueError(
                "The number of weights must be equal to the number of matrix columns."
            )

    def _normalize(self):
        """
        Normalizes the decision matrix based on the criteria types.

        Returns:
            np.ndarray: The normalized matrix.
        """
        norm_matrix = np.zeros_like(self.matrix, dtype=float)

        for j in range(self.matrix.shape[1]):
            if self.criteria[j].lower() == "benefit":
                norm_matrix[:, j] = self.matrix[:, j] / np.max(self.matrix[:, j])
            elif self.criteria[j].lower() == "cost":
                norm_matrix[:, j] = np.min(self.matrix[:, j]) / self.matrix[:, j]
            else:
                raise ValueError(
                    f"Invalid criteria type: {self.criteria[j]}. Must be 'benefit' or 'cost'."
                )

        return norm_matrix

    def _calculate_preference(self, norm_matrix):
        """
        Calculates the preference values based on the normalized matrix and weights.

        Args:
            norm_matrix (np.ndarray): The normalized matrix.

        Returns:
            np.ndarray: The preference values.
        """
        return np.sum(norm_matrix * self.weight, axis=1)

    def rank_score(self, preference):
        """
        Ranks the preference values.

        Args:
            preference (np.ndarray): The preference values.

        Returns:
            np.ndarray: The ranks of the alternatives.
        """
        sorted_indices = np.argsort(preference)
        sorted_indices = sorted_indices[::-1]
        ranks = np.zeros_like(sorted_indices, dtype=int)
        for i, index in enumerate(sorted_indices):
            ranks[index] = i + 1
        return ranks

    def calculate(self):
        """
        Performs the complete SAW calculation.

        Returns:
            tuple: A tuple containing the normalized matrix and the preference values.
        """
        norm_matrix = self._normalize()
        preference = self._calculate_preference(norm_matrix)
        ranks = self.rank_score(preference)
        return norm_matrix, preference, ranks

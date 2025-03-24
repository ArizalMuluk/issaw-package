import numpy as np

class SAW:
    """
    A class for performing Simple Additive Weighting (SAW) calculations.
    """

    def __init__(self, matrix, criteria, weight, normalize_weights=True):
        """
        Initializes the SAW object with the decision matrix, criteria, and weights.

        Args:
            matrix (list or np.ndarray): The decision matrix. Can be a list of lists or a NumPy array.
            criteria (list[str]): A list of criteria types ('benefit' or 'cost').
            weights (list[float]): A list of weights for each criterion.
            normalize_weights (bool, optional): Whether to normalize the weights to sum to 1. Defaults to True.

        Raises:
            TypeError: If matrix, criteria, or weights have incorrect types.
            ValueError: If the input data is invalid (e.g., incorrect lengths, non-numeric values, invalid criteria).
        """
        if not isinstance(matrix, (list, np.ndarray)):
            raise TypeError("Matrix must be a list or a NumPy array")
        if not isinstance(criteria, list) or not all(isinstance(c, str) for c in criteria):
            raise TypeError("Criteria must be a list of strings.")
        if not isinstance(weight, list) or not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError("Weights must be a list of numbers.")

        self.matrix = np.array(matrix, dtype=float)
        
        if self.matrix.ndim != 2:
            raise ValueError("Matrix must be a 2D array.")
        if self.matrix.shape[0] < 2:
            raise ValueError("Matrix must have at least 2 rows")
        if not np.issubdtype(self.matrix.dtype, np.number):
            raise ValueError("Matrix must contain only numeric values.")
            
        self.criteria = [c.lower() for c in criteria]
        self.weight = np.array(weight, dtype=float)

        if len(self.criteria) != len(self.weight):
            raise ValueError(
                "The number of criteria must be equal to the number of weights."
            )

        if len(self.weight) != self.matrix.shape[1]:
            raise ValueError(
                "The number of weights must be equal to the number of matrix columns."
            )
            
        if not all(c in ["benefit","cost"] for c in self.criteria):
            raise ValueError("Criteria must be 'benefit' or 'cost'")
        if not np.all(self.weight >= 0):
            raise ValueError("Weights must be non-negative.")
        if normalize_weights:
            self.weight /= np.sum(self.weight)

    def _normalize(self):
        """
        Normalizes the decision matrix based on the criteria types.

        Returns:
            np.ndarray: The normalized matrix.
        """
        norm_matrix = np.zeros_like(self.matrix, dtype=float)
        epsilon = 1e-10

        for j in range(self.matrix.shape[1]):
            if self.criteria[j] == "benefit":
                max_val = np.max(self.matrix[:, j])
                if max_val == 0:
                    norm_matrix[:, j] = 0
                else:
                    norm_matrix[:, j] = self.matrix[:, j] / max_val
            elif self.criteria[j] == "cost":
                min_val = np.min(self.matrix[:, j])
                if np.any(self.matrix[:, j] == 0):
                    norm_matrix[:, j] = min_val / (self.matrix[:, j] + epsilon)
                    norm_matrix[:, j] = min_val / self.matrix[:, j]
            else:
                raise ValueError(f"Invalid criteria type: {self.criteria[j]}. Must be 'benefit' or 'cost'.")

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
        sorted_indices = np.argsort(preference)[::-1]
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
    
# issaw: Simple Additive Weighting (SAW) Library

**issaw** is a Python library for implementing the Simple Additive Weighting (SAW) method for Multi-Criteria Decision Making (MCDM). It provides a robust and efficient way to normalize decision matrices, calculate preference values, and rank alternatives based on their preference scores. The library includes comprehensive input validation and error handling to ensure reliable results.

## Features

- **Robust Input Validation:** Thorough checks for data type, dimensions, and value validity (e.g., non-negative weights, numeric matrix values). Provides informative error messages for invalid inputs.
- **Flexible Weight Handling:** Accepts custom weights for each criterion, allowing users to reflect the relative importance of different criteria. Supports automatic weight normalization to sum to 1.
- **Efficient NumPy Implementation:** Leverages NumPy for efficient array operations, resulting in faster computation, especially for larger datasets.
- **Clear and Concise API:** Provides a straightforward interface for calculating SAW scores and ranks.
- **Handles Zero Values:** Includes robust handling of zero values in the decision matrix to avoid division by zero errors.


## Installation

You can install `issaw` directly from the GitHub repository using pip:

```bash
pip install git+https://github.com/ArizalMuluk/issaw-package.git


```
<!-- You can install `issaw` using pip:

```bash
pip install issaw
``` -->

## Usage

```python
import numpy as np
from issaw import SAW

# Decision matrix
matrix = np.array([[8, 7, 9, 6], [7, 8, 6, 8], [9, 6, 8, 7], [6, 9, 7, 9]])

# Criteria types ('benefit' or 'cost')
criteria = ["benefit", "benefit", "benefit", "benefit"]

# Weights for each criterion
weights = [0.3, 0.25, 0.25, 0.2]

# Initialize SAW object (normalize weights automatically)
saw = SAW(matrix, criteria, weights)

# Perform SAW calculation
normalized_matrix, preference_values, ranks = saw.calculate()

# Print results
print("Normalized Matrix:\n", normalized_matrix)
print("Preference Values:\n", preference_values)
print("Ranks:\n", ranks)
```

## Output

The `calculate()` method now returns a tuple containing:

- **normalized_matrix**: The normalized decision matrix.
- **preference_values**: The preference values for each alternative.
- **ranks**: The ranks of the alternatives (1 being the best).


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Version

0.2.1

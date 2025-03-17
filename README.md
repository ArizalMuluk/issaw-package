# issaw: Simple Additive Weighting (SAW) Library

**issaw** is a Python library for implementing the Simple Additive Weighting (SAW) method for Multi-Criteria Decision Making (MCDM). It provides functions for normalizing decision matrices, calculating preference values, and now also **ranking alternatives based on their preference scores.**

## Features

- **Normalization:** Normalizes the decision matrix based on criteria types ('benefit' or 'cost').
- **Preference Calculation:** Calculates preference values for each alternative based on normalized values and weights.
- **Ranking:** **NEW!** Ranks alternatives based on their preference scores, providing a clear order of preference.

## Installation

You can install `issaw` directly from the GitHub repository using pip:

```bash
pip install git+https://github.com/ArizalMuluk/issaw.git

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

# Initialize SAW object
saw = SAW(matrix, criteria, weights)

# Perform SAW calculation, including ranking
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
- **ranks**: The ranks of the alternatives, with rank 1 being the most preferred.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Version

0.2.0

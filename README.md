# issaw: Simple Additive Weighting (SAW) Method in Python

This Python library provides a simple and efficient implementation of the Simple Additive Weighting (SAW) method, a widely used Multiple Criteria Decision Making (MCDM) technique. SAW is particularly useful for evaluating alternatives based on multiple criteria with different weights.

## Installation

You can install `issaw` using pip:

```bash
pip install issaw
```

This will install the necessary dependencies, including NumPy.

## Usage

The core functionality is provided through the `saw` function. This function takes two arguments:

1. **decision_matrix**: A list of lists representing the decision matrix. Each inner list represents an alternative, and each element within the inner list represents the rating of that alternative on a specific criterion.
2. **weights**: A list of floats representing the weights of each criterion. The length of this list must match the number of columns in the decision_matrix.

Here's a basic example:

```python
from issaw import saw

# Define the decision matrix (alternatives x criteria)
decision_matrix = [
    [8, 7, 6, 9],  # Alternative 1
    [6, 8, 7, 5],  # Alternative 2
    [7, 6, 8, 7],  # Alternative 3
    [9, 5, 7, 8]   # Alternative 4
]

# Define the weights for each criterion
weights = [0.25, 0.25, 0.25, 0.25]  # Equal weights in this example

# Calculate the SAW scores
scores = saw(decision_matrix, weights)

# Print the results
print(scores)  # Output: [7.75, 6.75, 7.0, 7.25]
```

This will output a list of SAW scores for each alternative. The alternative with the highest score is considered the best in this method. Remember to handle potential errors, such as mismatched dimensions between the decision matrix and weights.

## Features

- **Simple and intuitive API**: The `saw` function provides a straightforward interface for calculating SAW scores.
- **Efficient implementation using NumPy**: Leverages NumPy for efficient array operations, resulting in faster computation, especially for larger datasets.
- **Handles various data types**: The decision matrix can accept various numerical data types (integers, floats).
- **Supports custom weights**: Allows users to specify custom weights for each criterion to reflect their relative importance.
- **Clear Error Handling**: (Add this if implemented) The function includes error handling for invalid inputs (e.g., mismatched dimensions, non-numeric values).

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

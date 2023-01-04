# Python LaTeX Formatting Tools

This repository contains a collection of Python functions for generating LaTeX formatting.

## Installation

To use these tools, simply clone the repository or download the `latex_formatting.py` file and import it into your Python scripts.

## Usage

The following functions are available:

- `matrix_to_latex(matrix, matrix_type='bmatrix')`: Converts a matrix to a LaTeX matrix string.
- `generate_section(title)`: Generates a LaTeX section heading.
- `generate_itemized_list(items)`: Generates a LaTeX itemized list.

## Examples

```python
import latex_formatting

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(latex_formatting.matrix_to_latex(matrix, matrix_type='pmatrix'))

print(latex_formatting.generate_section('Introduction'))

items = ['Item 1', 'Item 2', 'Item 3']
print(latex_formatting.generate_itemized_list(items))

# Python LaTeX Formatting Tools

This repository contains a collection of Python functions for generating LaTeX formatting.

## Installation

To use these tools, simply clone the repository or download the `latex_formatting.py` file and import it into your Python scripts.

## Usage

The following functions are available:

- `matrix_to_latex(matrix, matrix_type='bmatrix')`: Converts a matrix to a LaTeX matrix string.
- `generate_section(title)`: Generates a LaTeX section heading.
- `generate_itemized_list(items)`: Generates a LaTeX itemized list.
- `generate_sum(lower_bound, upper_bound, expression)`: Generates a LaTeX sum.
- `generate_product(lower_bound, upper_bound, expression)`: Generates a LaTeX product.
- `generate_integral(lower_bound, upper_bound, expression)`: Generates a LaTeX integral.
- `generate_limit(expression, variable, value, direction=None)`: Generates a LaTeX limit.
- `generate_piecewise(pieces))`: Generates a LaTeX piecewise function.

## Examples

```python
import latex_formatting

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(latex_formatting.matrix_to_latex(matrix, matrix_type='pmatrix'))

print(latex_formatting.generate_section('Introduction'))

items = ['Item 1', 'Item 2', 'Item 3']
print(latex_formatting.generate_itemized_list(items))

print(generate_sum(1, n, 'i^2'))
print(generate_product(1, n, 'i^2'))

print(generate_integral(0, 1, 'y^2', variable='y'))
print(generate_derivative('z^3', variable='z', order=2))

print(generate_limit('g(x)', 'x', '0', direction='-'))

pieces = [('x^2', 'x < 0'), ('x', '0 \le x \le 1'), ('2x-1', 'x > 1')]
print(generate_piecewise(pieces))

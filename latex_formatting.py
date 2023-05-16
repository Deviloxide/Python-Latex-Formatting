def matrix_to_latex(matrix, matrix_type='bmatrix'):
    """Converts a matrix to a LaTeX matrix string.

    Args:
        matrix: A 2D list or tuple representing the matrix.
        matrix_type: The type of matrix environment to use. Defaults to 'bmatrix'.

    Returns:
        A string containing the LaTeX matrix representation of the input matrix.
    """
    # Begin matrix environment
    latex = f'\\begin{{{matrix_type}}}'

    # Iterate over rows
    for row in matrix:
        # Add each element in the row to the string, separated by &
        latex += ' & '.join([str(elem) for elem in row]) + ' \\\\'

    # End matrix environment
    latex += f'\\end{{{matrix_type}}}'

    return latex

def generate_section(title):
    """Generates a LaTeX section heading.

    Args:
        title: The title of the section.

    Returns:
        A string containing the LaTeX representation of the section heading.
    """
    return f'\\section{{{title}}}'

def generate_itemized_list(items):
    """Generates a LaTeX itemized list.

    Args:
        items: A list of strings representing the items in the list.

    Returns:
        A string containing the LaTeX representation of the itemized list.
    """
    latex = '\\begin{itemize}'
    for item in items:
        latex += f'\n\\item {item}'
    latex += '\n\\end{itemize}'
    return latex

def generate_sum(lower_bound, upper_bound, variable, expression):
    """Generates a LaTeX representation of a summation.

    Args:
        lower_bound: The lower bound of the summation.
        upper_bound: The upper bound of the summation.
        expression: The expression to be summed.

    Returns:
        A string containing the LaTeX representation of the summation.
    """
    return f'\\sum_{{{lower_bound}}}^{{{upper_bound}}} {expression}'

def generate_product(lower_bound, upper_bound, variable, expression):
    """Generates a LaTeX representation of a product.

    Args:
        lower_bound: The lower bound of the product.
        upper_bound: The upper bound of the product.
        expression: The expression to be multiplied.

    Returns:
        A string containing the LaTeX representation of the product.
    """
    return f'\\prod_{{{lower_bound}}}^{{{upper_bound}}} {expression}'

def generate_integral(lower_bound, upper_bound, expression, variable='x'):
    """Generates a LaTeX representation of an integral.

    Args:
        lower_bound: The lower bound of the integral.
        upper_bound: The upper bound of the integral.
        expression: The expression to be integrated.
        variable: The variable of integration (default 'x').

    Returns:
        A string containing the LaTeX representation of the integral.
    """
    return f'\\int_{{{lower_bound}}}^{{{upper_bound}}} {expression} d{{{variable}}}'

def generate_derivative(expression, variable='x', order=1):
    """Generates a LaTeX representation of a derivative.

    Args:
        expression: The expression to be differentiated.
        variable: The variable of differentiation (default 'x').
        order: The order of the derivative (default 1).

    Returns:
        A string containing the LaTeX representation of the derivative.
    """
    if order == 1:
        return f'\\frac{{d}}{{d{variable}}} {expression}'
    else:
        return f'\\frac{{d^{order}}}{{d{variable}^{order}}} {expression}'
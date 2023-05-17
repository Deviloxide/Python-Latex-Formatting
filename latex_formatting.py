def generate_matrix(matrix, matrix_type='bmatrix'):
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
   
def generate_limit(expression, variable, value, direction=None):
    """Generates a LaTeX representation of a limit.

    Args:
        expression: The expression to be evaluated.
        variable: The variable that the limit is taken with respect to.
        value: The value that the variable approaches.
        direction: The direction of the limit, either 'left' or 'right' (optional).

    Returns:
        A string containing the LaTeX representation of the limit.
    """
    limit_symbol = f'\\lim_{{{variable} \\rightarrow {value}'
    if direction:
        limit_symbol += f"^{direction}"
    limit_symbol += '}'
    return f'{limit_symbol} {expression}'

def generate_piecewise(pieces):
    """Generates a LaTeX representation of a piecewise function.

    Args:
        pieces: A list of tuples where each tuple contains the expression and condition for each piece.

    Returns:
        A string containing the LaTeX representation of the piecewise function.
    """
    piecewise = '\\begin{cases}\n'
    for i, piece in enumerate(pieces):
        expression, condition = piece
        piecewise += f'{expression}, & {condition} \\\\\n'
    piecewise += '\\end{cases}'
    return piecewise

def generate_multiintegral(integrals, expression):
    """Generates a LaTeX representation of multiple integrals using recursion.

    Args:
        integrals: A list of tuples where each tuple contains the integration variable and the limits of integration.
        expression: The expression being integrated.

    Returns:
        A string containing the LaTeX representation of the multiple integral.
    """
    if not integrals:
        return expression
    else:
        integral = integrals.pop(0)
        variable = integral[0]
        limits = (integral[1], integral[2])
        integral_symbol = f'\\int_{{{limits[0]}}}^{{{limits[1]}}} '
        return f'{integral_symbol} {generate_multiintegral(integrals, expression)} \\ d{{{variable}}}'

def generate_multiderivative(derivatives, expression):
    """Generates a LaTeX representation of multiple derivatives using recursion.

    Args:
        derivatives: A list of tuples where each tuple contains the differentiation variable and the number of times to differentiate.
        expression: The expression being differentiated.

    Returns:
        A string containing the LaTeX representation of the multiple derivative.
    """
    if not derivatives:
        return expression
    else:
        derivative = derivatives.pop(0)
        variable = derivative[0]
        order = derivative[1]
        derivative_symbol = ''
        if order == 1:
            derivative_symbol = f'\\frac{{d}}{{d{variable}}}'
        else:
            derivative_symbol = f'\\frac{{d^{{{order}}}}}{{d{variable}^{{{order}}}}}'
        if (len(derivatives) == 0):
            return f'{derivative_symbol} {generate_multiderivative(derivatives, expression)}'
        return f'{derivative_symbol} ({generate_multiderivative(derivatives, expression)})'

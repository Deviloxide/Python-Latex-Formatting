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

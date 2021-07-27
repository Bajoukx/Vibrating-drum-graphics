import scipy.sparse
import scipy.sparse.linalg

import drum


def get_scipy_finite_differences_matrix(square_drum):
    """Gets a scipy implementation of the finite differences matrix."""
    matrix_size = square_drum.grid_sample_points**2
    main_diagonals = scipy.sparse.diags([1, -4, 1], [-1, 0, 1],
                                        (matrix_size, matrix_size))

    offset_diagonal = square_drum.grid_sample_points
    upper_diagonal = scipy.sparse.diags([1], [offset_diagonal],
                                        (matrix_size, matrix_size))
    lower_diagonal = scipy.sparse.diags([1], [-offset_diagonal],
                                        (matrix_size, matrix_size))

    matrix = main_diagonals + upper_diagonal + lower_diagonal
    matrix = -matrix / square_drum.step_size**2

    return matrix


def solve_eigsh(square_drum, n_eigenvalues):
    """Solves equation in order of eigenvalues and eigenvectors."""
    if not isinstance(square_drum, drum.SquareDrum):
        raise TypeError('Inappropriate type.')
    return scipy.sparse.linalg.eigsh(
        get_scipy_finite_differences_matrix(square_drum),
        n_eigenvalues,
        which='SM',
        return_eigenvectors=True)

import numpy as np
import scipy


def get_drum_mesh(grid_sample_points):
    x_grid = np.linspace(-1, 1, grid_sample_points)
    y_grid = np.linspace(-1, 1, grid_sample_points)

    x_mesh_matrix, y_mesh_matrix = np.meshgrid()
    return x_mesh_matrix, y_mesh_matrix

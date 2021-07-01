"""Drum definition module."""
import numpy as np


class SquareDrum:
    """Class of a square shaped drum.

    A square drum with a width size, sampled and represented in a numpy
    mesh grid.
    """
    def __init__(self, grid_sample_points=256, width=1):
        """Initializes the square drum mesh.

        Attributes:
            grid_sample_points: The number of points to sample in each axis.
            width: The width of the square.
            step_size: Distance between sample points.
         """
        self.grid_sample_points = grid_sample_points
        self.width = width
        self.step_size = self.width / self.grid_sample_points

    def get_mesh(self):
        """Gets the numpy mesh of the drum."""
        x_grid = np.linspace(0, self.width, self.grid_sample_points)
        y_grid = np.linspace(0, self.width, self.grid_sample_points)

        x_mesh_matrix, y_mesh_matrix = np.meshgrid(x_grid, y_grid)
        return x_mesh_matrix, y_mesh_matrix

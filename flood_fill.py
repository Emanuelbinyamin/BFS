# Flood Fill Algorithm
# This function implements a graph traversal approach to "flood-fill" an image, similar to the paint bucket tool in graphics software.
def flood_fill(image, row, col, new_color):
    """
    Perform flood fill on a 2D image.

    Parameters:
    - image (list[list[int]]): The 2D grid representation of the image.
    - row (int): The starting row for flood fill.
    - col (int): The starting column for flood fill.
    - new_color (int): The color to replace the original region.

    Returns:
    - list[list[int]]: The updated image after flood fill.
    """
    # Starting pixel's color
    start_color = image[row][col]
    # Queue for BFS traversal
    queue = [(row, col)]
    # Visited set to prevent re-visiting nodes
    visited = set()

    while queue:
        current_row, current_col = queue.pop(0)  # Dequeue the first pixel
        visited.add((current_row, current_col))  # Mark as visited

        # Change the color of the current pixel
        image[current_row][current_col] = new_color

        # Check all valid neighbors and enqueue them
        for neighbor_row, neighbor_col in get_neighbors(image, current_row, current_col, start_color):
            if (neighbor_row, neighbor_col) not in visited:
                queue.append((neighbor_row, neighbor_col))

    return image


def get_neighbors(image, row, col, start_color):
    """
    Get valid neighboring pixels with the same starting color.

    Parameters:
    - image (list[list[int]]): The 2D grid representation of the image.
    - row (int): Current row.
    - col (int): Current column.
    - start_color (int): The color of the starting pixel.

    Returns:
    - list[tuple[int, int]]: Valid neighbors.
    """
    potential_neighbors = [
        (row - 1, col),  # Up
        (row + 1, col),  # Down
        (row, col - 1),  # Left
        (row, col + 1)   # Right
    ]

    return [
        (n_row, n_col) for n_row, n_col in potential_neighbors
        if is_valid_pixel(image, n_row, n_col) and image[n_row][n_col] == start_color
    ]


def is_valid_pixel(image, row, col):
    """
    Check if the pixel is within image boundaries.

    Parameters:
    - image (list[list[int]]): The 2D grid representation of the image.
    - row (int): Row index.
    - col (int): Column index.

    Returns:
    - bool: True if the pixel is valid; False otherwise.
    """
    return 0 <= row < len(image) and 0 <= col < len(image[0])

# Example usage:
if __name__ == "__main__":
    # Example grid (image)
    example_image = [
        [1, 0, 2, 2, 0],
        [0, 0, 2, 2, 0],
        [0, 2, 2, 2, 2],
        [0, 0, 2, 0, 2],
        [1, 0, 0, 0, 0]
    ]

    print("Original Image:")
    for row in example_image:
        print(row)

    # Apply flood fill starting at (2, 2) with a new color 9
    result = flood_fill(example_image, 2, 2, 9)

    print("\nFlood-Filled Image:")
    for row in result:
        print(row)

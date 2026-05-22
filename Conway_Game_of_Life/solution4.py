# Conway's Game of Life — human-style version


def next_world(current_world):
    """
    Creates the next version of the world.
    Each cell decides whether it lives or dies.
    """

    height = len(current_world)
    width = len(current_world[0])

    # Prepare a fresh empty world
    next_world = []

    # Go row by row
    for row_index in range(height):

        new_row = []

        # Go cell by cell
        for col_index in range(width):

            # Look around this cell (its 8 neighbors)
            alive_count = 0

            # Scan the 3x3 square around the cell
            for r in range(row_index - 1, row_index + 2):
                for c in range(col_index - 1, col_index + 2):

                    # Skip the cell itself
                    if r == row_index and c == col_index:
                        continue

                    # Ignore positions outside the grid
                    if r < 0 or r >= height or c < 0 or c >= width:
                        continue

                    # Count alive neighbors
                    if current_world[r][c] == 1:
                        alive_count += 1

            # Now decide this cell's fate

            current_cell = current_world[row_index][col_index]

            if current_cell == 1:
                # Alive cell rules
                if alive_count < 2:
                    new_row.append(0)  # dies (lonely)
                elif alive_count > 3:
                    new_row.append(0)  # dies (overcrowded)
                else:
                    new_row.append(1)  # survives
            else:
                # Dead cell rule
                if alive_count == 3:
                    new_row.append(1)  # becomes alive
                else:
                    new_row.append(0)  # stays dead

        # Add the completed row to the new world
        next_world.append(new_row)

    return next_world


def show(world):
    """
    Print the world in a more visual way.
    Alive = █
    Dead  = .
    """

    for row in world:
        line = ""
        for cell in row:
            if cell == 1:
                line += "█ "
            else:
                line += ". "
        print(line)
    print()


# Starting pattern (glider)
world = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]


# Run simulation
for step in range(6):
    print(f"Generation {step}")
    show(world)

    world = next_world(world)
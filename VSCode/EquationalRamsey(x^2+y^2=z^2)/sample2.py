import random

def is_color_allowed(z, color, COL):
    """
    Check if the given color is allowed for integer z.
    """
    for x in range(1, z):
        for y in range(x, z):
            if x**2 + y**2 == z**2:
                if COL.get(x) == color and COL.get(y) == color:
                    return False
    return True

def randomized_greedy_coloring(n, num_colors):
    """
    Perform randomized greedy coloring of integers from 1 to n using up to num_colors colors.
    """
    # Initialize coloring dictionary
    COL = {}
    COL[1] = 1  # Start by coloring 1 with color 1

    for z in range(2, n + 1):
        # Randomize color selection
        colors = list(range(1, num_colors + 1))
        random.shuffle(colors)  # Shuffle the colors to pick randomly

        color_found = False
        for color in colors:
            if is_color_allowed(z, color, COL):
                COL[z] = color
                color_found = True
                break
        
        if not color_found:
            # If no color was available, exit with the last successful coloring
            print(f"Cannot color past {z - 1}")
            return (z - 1, COL)
    
    return (n, COL)

# Parameters
n = 20000
num_colors = 5

# Perform coloring
result = randomized_greedy_coloring(n, num_colors)

# Print results
print("Coloring:")
for i in range(1, result[0] + 1):
    print(f"COL({i}) = {result[1].get(i, 'uncolored')}")
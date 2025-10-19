import math
n = 100
colored = [True] * n

def greedy_coloring(n, num_colors):
    COL = {}
    for i in range(1, n+1):
        COL[i] = 1  # Initially assign color 1 to all

    for a in range(1, n + 1):
        for d in range(1, a+1):
            x = a + 5*d
            y = a + 3*d

            if x <= n and y <= n:
                # Retrieve the colors of a, x, y
                color_a = COL.get(a)
                color_x = COL.get(x)
                color_y = COL.get(y)

                # Check if all three colors are the same
                if color_a == color_x == color_y:
                    # Find a new color for x that is different from color_a
                    new_color = None
                    for color in range(1, num_colors + 1):
                        if color != color_a:
                            new_color = color
                            break
                    
                    if new_color is None or color_x == new_color:
                        print(f"Cannot color past {x} with x={x}, a={a}, y={y}")
                        return (x - 1, COL)
                    else:
                        COL[x] = new_color
                        colored[x] = False

    return (n, COL)

num_colors = 3
result = greedy_coloring(n, num_colors)
print("Coloring:")
for i in range(1, result[0] + 1):
    print(f"COL({i}) = {result[1][i]}")
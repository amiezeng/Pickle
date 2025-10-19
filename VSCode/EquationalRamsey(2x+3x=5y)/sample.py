import math
import random
n = 100
colored = [True] * (n+1)

def greedy_coloring(n, num_colors):
    COL = {}
    for i in range(1, n+1):
        COL[i] = 1  # Initially assign color 1 to all

    for a in range(1, n + 1):
        for d in range(1, a+1):
            x = a + 5*d
            y = a + 3*d

            if x <= n and y <= n:
                # Check if the colors of a, x, y are not all the same
                if COL.get(a) != COL.get(y):
                    new_color = new_color = random.randint(1,3)
                    COL[x] = new_color
                    colored[x] = False
                if COL.get(a) == COL.get(x) == COL.get(y):
                    # Change the color of x to ensure they are not all the same
                    if COL[a] != 1 and colored[x] == True:
                        new_color = 1 
                    else:
                        new_color = 2
                    if new_color > num_colors or (COL.get(x) == new_color):
                        print(f"Cannot color past {x} with x={x}, a={a}, y={y}")
                        return (x - 1, COL)
                    else:
                        COL[x] = new_color
                        colored[x] = False

    return (n, COL)

num_colors = 2
result = greedy_coloring(n, num_colors)
print("Coloring:")
for i in range(1, result[0] + 1):
    print(f"COL({i}) = {result[1][i]}")
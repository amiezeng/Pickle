import math
import random

def greedy_coloring(n, num_colors):
    # Initialize coloring for 1, 2, ..., z-1
    COL = {}
    for i in range(1, 21):
        COL[i] = random.randint(1, 2)

    for z in range(2, n + 1):
        color_1_allowed = True
        color_2_allowed = True

        for x in range(1, z):
            for y in range(x, z):
                if x**2 + y**2 == z**2:
                    if COL.get(x) == COL.get(y) == 1:
                        color_1_allowed = False
                    if COL.get(x) == COL.get(y) == 2:
                        color_2_allowed = False
        
        if not color_1_allowed and not color_2_allowed:
            print(f"Cannot color past {z - 1}")
            return (z - 1, COL)
    
    return (n, COL)

n = 30
num_colors = 2
result = greedy_coloring(n, num_colors)
print("Coloring:")
for i in range(1, result[0] + 1):
    print(f"COL({i}) = {result[1][i]}")
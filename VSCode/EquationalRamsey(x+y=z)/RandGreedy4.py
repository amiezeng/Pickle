import math
import random

def greedy_coloring(n, num_colors):
    # Initialize coloring for 1, 2, ..., z-1
    COL = {}
    COL[1] = 1

    for z in range(2, n + 1):
        color_1_allowed = True
        color_2_allowed = True
        color_3_allowed = True
        color_4_allowed = True

        for x in range(1, z):
            for y in range(x, z):
                if x + y == z:
                    if COL.get(x) == COL.get(y) == 1:
                        color_1_allowed = False
                    elif COL.get(x) == COL.get(y) == 2:
                        color_2_allowed = False
                    elif COL.get(x) == COL.get(y) == 3:
                        color_3_allowed = False
                    elif COL.get(x) == COL.get(y) == 4:
                        color_4_allowed = False
        
                if color_1_allowed and color_2_allowed and color_3_allowed and color_4_allowed:
                    COL[z] = random.randint(1,4)
                elif color_1_allowed and color_2_allowed and color_3_allowed:
                    COL[z] = random.randint(1,3)
                elif color_1_allowed and color_2_allowed:
                    COL[z] = random.randint(1,2)
                elif color_1_allowed and color_3_allowed:
                    COL[z] = random.choice([1, 3])
                elif color_1_allowed and color_4_allowed:
                    COL[z] = random.choice([1, 4])

                elif color_2_allowed and color_3_allowed and color_4_allowed:
                    COL[z] = random.randint(2,4)
                elif color_2_allowed and color_3_allowed:
                    COL[z] = random.randint(2,3)
                elif color_2_allowed and color_4_allowed:
                    COL[z] = random.choice([2, 4])

                elif color_3_allowed and color_4_allowed:
                    COL[z] = random.choice([3, 4])

                
                elif color_1_allowed:
                    COL[z] = 1
                elif color_2_allowed:
                    COL[z] = 2
                elif color_3_allowed:
                    COL[z] = 3
                elif color_4_allowed:
                    COL[z] = 4
                else:
                    print(f"Cannot color past {z - 1} with x={x}, y={y}, z={z}")
                    return (z - 1, COL)
    
    return (n, COL)

n = 8000
num_colors = 4
result = greedy_coloring(n, num_colors)
print("Coloring:")
for i in range(1, result[0] + 1):
    print(f"COL({i}) = {result[1][i]}")
import pygame

def prims(matrixx):
    matrix = matrixx.copy()
    print(matrix)
    selected = [(0,0)]
    temp = []
    tempco = []
    Xrows = [0]
    animated = []
    while len(selected) < len(matrix[0]):
        temp = []
        tempco = []
        for i in range(len(matrix)):
            if i not in Xrows:
                for j in range(len(matrix)):
                    if j in Xrows and matrix[i][j] != 0:
                        temp.append(matrix[i][j])
                        tempco.append([i,j])
        if not temp:
            return ("Not connected graph", False)
        animated.extend(tempco)
        min_number = temp.index(min(temp))
        selected.append(tempco[min_number])
        tempco[min_number].append(True)
        animated.append(tempco[min_number])
        Xrows.append(tempco[min_number][0])
    return animated

def floyds(matrixx):
    matrix = [row[:] for row in matrixx]
    if len(matrix) == 0:
        return ("Matrix empty", False)
    numOfNodes= len(matrix)
    route_table = [[i for j in range(numOfNodes)]for i in range(numOfNodes)]
    matrix = [[matrix[i][j] if i!=j and matrix[i][j] != 0 else float('inf') for j in range(numOfNodes)]for i in range(numOfNodes)]


    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[k][j]+matrix[i][k] < matrix[i][j]:
                    matrix[i][j] = matrix[k][j]+matrix[i][k]
                    route_table[i][j] = route_table[k][j]
    return matrix,route_table


test_matrix = [
    [0, 5, 0, 10],  # Node 0
    [5, 0, 3, 0],    # Node 1
    [0, 3, 0, 1],    # Node 2
    [10, 0, 1, 0]    # Node 3
]

matrix,route_table = floyds(test_matrix)
for row in matrix:
    print(row)
print("-------------------------------------")
for row in route_table:
    print(row)
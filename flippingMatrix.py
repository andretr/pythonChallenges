def flippingMatrix(matrix):
    # Write your code here
    sumTotal, max_val = 0, 0
    for i in range(int(len(matrix)/2)):
        for j in range(int(len(matrix)/2)):
            max_val = matrix[i][j]
    matrix[i].reverse()
    if(matrix[i][j] > max_val):
        max_val = matrix[i][j]
    matrix.reverse()
    if(matrix[i][j] > max_val):
        max_val = matrix[i][j]
    matrix[i].reverse()
    if(matrix[i][j] > max_val):
        max_val = matrix[i][j]
    sumTotal += max_val
    return sumTotal

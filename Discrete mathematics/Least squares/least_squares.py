import numpy as np

def permutation_of_rows(u_matrix, row, col, shift_counter):
    for r in range(row + 1, n):
        if u_matrix[r][col] != 0:
            u_matrix[[row, r]] = u_matrix[[r, row]]
            break
    else:
        shift_counter += 1
    return u_matrix, shift_counter

def direct_pass(matrix):
    u_matrix = matrix.copy()
    shift_counter = 0
    for row in range(n):
        col = row + shift_counter
        while col < (m - 1) and u_matrix[row][col] == 0:
            u_matrix, shift_counter = permutation_of_rows(u_matrix,
                                                          row,
                                                          col,
                                                          shift_counter)
            col = row + shift_counter
        for next_row in range(row + 1, n):
            if col < m and u_matrix[row][col] != 0:
                multiplier = u_matrix[next_row][col] / u_matrix[row][col]
                subtrahend = u_matrix[row].copy()
                subtrahend *= multiplier
                u_matrix[next_row] -= subtrahend
    return u_matrix

def return_pass(u_matrix):
    results = [1] * (m + 1)

    col = m - 1
    for row in range(len(u_matrix) - 1, -1, -1):
        u_matrix[row] *= results
        for j in range(col + 1, m):
            u_matrix[row][m] -= u_matrix[row][j]
        results[col] = u_matrix[row][m] / u_matrix[row][col]
        col -= 1
    results.pop()
    return results

def gaussian_elim(matrix):

    u_matrix = direct_pass(matrix)
    results = return_pass(u_matrix)

    return results

def least_squares(matrix):

    global n, m
    coef_matrix = matrix[:, :-1].T.dot(matrix[:, :-1])
    n = m = len(coef_matrix)
    const_terms = matrix[:, :-1].T.dot(matrix[:, -1])

    proj_matrix = np.concatenate((coef_matrix, const_terms.reshape(len(const_terms),1)), axis = 1)

    results = gaussian_elim(proj_matrix)

    return results


n, m = [int(i) for i in input().split()]

matrix = []
for _ in range(n):
    equ = [float(i) for i in input().split()]
    matrix.append(equ)
matrix = np.array(matrix)

results = least_squares(matrix)
print(' '.join([str(result) for result in results]))

from fractions import Fraction

# проверяем есть ли полностью нулевые столбцы
# удаляем, если такие найдутся
# inf_flag = 1 (если такая система имеет решения, то их бесконечно много)
def check_column(system):
    global m, inf_flag
    list_for_drop = []
    for c in range(m):
        if system[0][c] == 0:
            for r in range(1, n):
                if system[r][c] != 0:
                    break
            else:
                list_for_drop.append(c)
                inf_flag = 1
                m -= 1
    for i in list_for_drop:
        for r in range(n):
            system[r].pop(i)
    return system

def check_rows(matrix):
    global n
    to_drop = []
    for r, row in enumerate(matrix):
        summ = 0
        for col in row:
            summ += abs(col)
        if summ == 0:
            to_drop.append(r)
            n -= 1
    for r in reversed(to_drop):
        matrix.pop(r)
    return matrix
            

# меняем местами строки, чтобы при переменной оказался не нулевой коэффициент
def permutation_of_rows(U, row, col, shift_counter):
    for r in range(row + 1, n):
        if U[r][col] != 0:
            U.insert(row, U.pop(r))
            break
    else:
        shift_counter += 1
    return U, shift_counter

# прямой проход
def direct_pass(system):
    U = system.copy()
    shift_counter = 0
    for row in range(n):
        col = row + shift_counter
        while col < (m - 1) and U[row][col] == 0:
            U, shift_counter = permutation_of_rows(U, row, col, shift_counter)
            col = row + shift_counter
        for next_row in range(row + 1, n):
            if col < m and U[row][col] != 0:
                multiplier = Fraction(U[next_row][col] / U[row][col])
                subtrahend = U[row].copy()
                for c in range(m + 1):
                    subtrahend[c] =  Fraction(subtrahend[c] * multiplier)
                    U[next_row][c] = Fraction(U[next_row][c] - subtrahend[c])
    return U

# обратный проход
def return_pass(U):
    U = list(reversed(U))
    results = [1] * m

    col = m - 1
    for row in U:
        for i in range(m):
            row[i] = Fraction(row[i] * results[i])
        for j in range(col + 1, m):
            row[m] = Fraction(row[m] - row[j])
        results[col] = Fraction(row[m] / row[col])
        col -= 1

    return results
    
def dimension_search(matrix, col):
    rank = n
    row = n - 1
    while matrix[row][col] == 0 and row != 0:
        rank -= 1
        row -= 1
    return rank

# метод исключения Гаусса
def gaussian_elim(system):
    answer = ''
    results = []

    U = direct_pass(system)
    U = check_rows(U)

    rank_of_matrix = dimension_search(U, m - 1)
    dim_of_const_terms = dimension_search(U, m)

    if rank_of_matrix == n:
        if inf_flag == 1 or m > n:
            answer = 'INF'
        else:
            answer = 'YES'
            results = return_pass(U)
    else:
        if rank_of_matrix < dim_of_const_terms:
            answer = 'NO'
        else:
            answer = 'INF'

    return answer, results

n, m = [int(i) for i in input().split()]
system = []

inf_flag = 0

for i in range(n):
    equation = [float(c) for c in input().split()]
    system.append(equation)

system = check_column(system)
answer, results = gaussian_elim(system)

if len(results) == 0:
    print(answer)
else:
    print(answer)
    print(' '.join([str(float(result)) for result in results]))

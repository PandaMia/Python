def permutation(n, k, seq = ''):

    if k > n:
        print()
    elif len(seq) == k:
        print(*seq)
    else:
        for elem in range(n):
            if str(elem) not in seq:
                permutation(n, k, seq = seq + str(elem))
 
n, k = [int(i) for i in input().split()]
perm = [int(i) for i in range(k)]
permutation(n, k)

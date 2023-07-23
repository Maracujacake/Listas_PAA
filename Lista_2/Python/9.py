def maiorSubs(A):
    def lis_recursive(i):
        if i == 0:
            return [A[0]], 1

        max_length = 1
        max_subsequence = [A[i]]
        for j in range(i):
            if A[j] < A[i]:
                subsequence, length = lis_recursive(j)
                if length + 1 > max_length:
                    max_length = length + 1
                    max_subsequence = subsequence + [A[i]]

        return max_subsequence, max_length

    n = len(A)
    max_length = 1
    max_subsequence = [A[0]]
    for i in range(n):
        subsequence, length = lis_recursive(i)
        if length > max_length:
            max_length = length
            max_subsequence = subsequence

    return max_subsequence

# Exemplo de uso:
A = [3, 4, 5, 8, 10, 9, 11]
print(maiorSubs(A))

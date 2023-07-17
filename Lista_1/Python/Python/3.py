array = [1, 3, 4, 6, 2, 5, 7]
def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i] # troca a posicao do menor elemento com o primeiro, segundo, conforme a ordem
    return A


print(selection_sort(array))

# complexidade: O(n^2), percorre o array inteiro por cada elemento
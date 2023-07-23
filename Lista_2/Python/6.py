# 729 * T(n/9) + 15 * n^3

# se a = b^d então T(n) = O(n^d log n)
# se a < b^d então T(n) = O(n^d)
# se a > b^d então T(n) = O(n^log_b a)

# a = 729, b = 9, c = 15, d = 3
# a <>= 9^3 (81 * 9 = 729)
# a = 729
# a complexidade obtida é de O(n^3 * logN)
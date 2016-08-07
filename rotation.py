 # CORRECT: 100%
 def solution_simple(A, K):
 	from collections import deque
 	rotated_A = deque(A)
 	rotated_A.rotate(K)
 	return list(rotated_A)

 # CORRECT: 100%
def solution(A, K):
	result = []
	len_A = len(A)

	for i, elem in enumerate(A):
		new_i = (i + 1 * K + len_A) % len_A
		result.insert(new_i, elem)

	return result


# OTHERS

# CORRECT: 100% NO COPY OF ARRAY
def reverse(arr, i, j):
    for idx in xrange((j - i + 1) / 2):
        arr[i + idx], arr[j - idx] = arr[j - idx], arr[i + idx]

def solution_5(A, K):
    l = len(A)
    if l == 0:
        return []

    K = K % l

    reverse(A, l - K, l -1)
    reverse(A, 0, l - K -1)
    reverse(A, 0, l - 1)

    return A

# INCORRECT: 25%
def solution_1(A, K):
	A_len = len(A)
	return [A[(K + i) % A_len] for i in range(len(A))]


# INCORRECT: 12%
def solution_2(A, K):
    n = K % len(A) - 1
    return A[n:] + A[:n]

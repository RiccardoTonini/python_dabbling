
# SIMPLE: Performance 20% Correctnes 80% Total 60%
def solution_1(A):
	from collections import Counter
	for k, v in Counter(A).iteritems():
		if v == 1:
			return k

# CORRECT: Performance 100% Correctnes 100%

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    from itertools import izip_longest
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def solution(A):
	A.sort(reverse=True)
	for i, j in grouper(A, 2):
		if i != j:
			return i

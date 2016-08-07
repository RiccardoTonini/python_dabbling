def solution(N):
    # write your code in Python 2.7
    bin_n = bin(N)[2:].strip('0')
    bits = bin_n.split('1')
    return len(max(bits))

def solution_2(N):
    found_one = False
    crrnt_slot_count = 0
    result = 0
    i = N
    while(i):
        if i & 1 == 1:
            if (found_one == False):
                found_one = True
            else:
                result = max(crrnt_slot_count, result)
            crrnt_slot_count = 0
        else:
            crrnt_slot_count += 1
        i >>= 1

    return result

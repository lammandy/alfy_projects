# def input_list():

#     def input_list_helper(nums):
#         while True:
#             num = input()
#             if num != ' ':
#                 nums.append(int(num))
#             else:
#                 break

#     nums = []
#     sum = 0
#     input_list_helper(nums)
#     for num in nums:
#         sum += num
#     nums.append(sum)
#     return nums

def check_monotonic_sequence(sequence):
    increasing = True
    decreasing = True
    strictly = True
    if sequence:
        prev = sequence[0]
        for num in sequence[1:]:
            increasing = increasing and num >= prev
            decreasing = decreasing and num <= prev
            strictly = strictly and num != prev
            if not increasing and not decreasing:
                break
            prev = num
    return [
        increasing,
        increasing and strictly,
        decreasing,
        decreasing and strictly,
    ]

def check_monotonic_sequence_inverse(def_bool):
    mi, smi, md, smd = def_bool
    if mi and smi and md and smd:
        return []
    if not mi and not smi and not md and not smd:
        return [1, 0, 1]
    if mi and smi and not md and not smd:
        return [0, 1]
    if mi and not smi and not md and not smd:
        return [0, 0, 1]
    if not mi and not smi and md and smd:
        return [1, 0]
    if not mi and not smi and md and not smd:
        return [1, 1, 0]
    if mi and not smi and md and not smd:
        return[1, 1]
    else:
        return None

def primes_generator(n):
    cnum = 1
    primes = []
    while len(primes) < n:
        cnum += 1
        is_prime = True
        for p in primes:
            if cnum % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(cnum)
    return primes

def is_empty_vector(vec_lst):

    prev_vec_length = len(vec_lst[0])
    for vec in vec_lst:
        if len(vec) != prev_vec_length:
            return True
        prev_vec_length = len(vec)
    return False

def vectors_list_sum(vec_lst):
    sum = []
    if not is_empty_vector(vec_lst):
        for i in range(len(vec_lst[0])):
            sum.append(0)
        for vec in vec_lst:
            for i, num in enumerate(vec):
                sum[i] += vec[i]

    return sum

def calc_the_inner_product(vec_1, vec_2):
    prod = 0
    if not is_empty_vector([vec_1, vec_2]):
        for i in range(len(vec_1)):
            prod += (vec_1[i] * vec_2[i])
    else:
        return None
    return prod

def orthogonal_number(vectors):
    ortho_pairs = 0
    for i in range(len(vectors))[:-1]:
        for j in range(len(vectors))[i+1:]:
            prod = calc_the_inner_product(vectors[i], vectors[j])
            if prod == 0:
                ortho_pairs += 1
    return ortho_pairs

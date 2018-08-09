def pair_sum(arr, total):
    pairs = {}
    valid_pairs = []
    num = 0
    for ele in arr:
        if ele in pairs:
            valid_pairs.append([ele, pairs[ele]])
            num += 1
        else:
            pairs[total - ele] = (ele)

    print(num, valid_pairs)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pair_sum(array, 15)

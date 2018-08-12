def large_cont_sum(arr):
    if len(arr) == 0:
        return None
    curr_sum = max_sum = arr[0]
    for num in arr[1:]:
        if curr_sum + num > num:
            curr_sum = curr_sum + num
        if curr_sum > max_sum:
            max_sum = curr_sum
    print(max_sum)

large_cont_sum([1,2,-1,3,4,10,10,-10,-1])

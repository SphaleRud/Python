def merge(left_list, right_list):  
    sorted_list = []
    Li = Ri = 0
    Ll, Rl = len(left_list), len(right_list)
    for i in range(Ll + Rl):
        if Li < Ll and Ri < Rl:
            if left_list[Li] <= right_list[Ri]:
                sorted_list.append(left_list[Li])
                Li += 1
            else:
                sorted_list.append(right_list[Ri])
                Ri += 1
        elif Li == Ll:
            sorted_list.append(right_list[Ri])
            Ri += 1
        elif Ri == Rl:
            sorted_list.append(left_list[Li])
            Li += 1
    return sorted_list

def merge_sort(nums):  
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)

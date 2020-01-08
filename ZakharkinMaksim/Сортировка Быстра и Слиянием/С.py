from random import *
def middle(num,N):
    return num/N
count=0
def partition(n, l, h):
    global count
    T = n[(l + h) // 2]
    i = l - 1
    j = h + 1
    while True:
        i += 1
        while n[i] < T:
            count+=1
            i += 1
        j -= 1
        while n[j] > T:
            count+=1
            j -= 1
        if i >= j:
            count+=1
            return j
        n[i], n[j] = n[j], n[i]

def quick_sort(n):
    global count
    def quick_sort2(i, l, h):
        if l < h:
            split = partition(i, l, h)
            quick_sort2(i, l, split)
            quick_sort2(i, split + 1, h)
            count+=1
    quick_sort2(n, 0, len(n) - 1)

count2=0
def merge(left_list, right_list):  
    sorted_list = []
    Li = Ri = 0
    Ll, Rl = len(left_list), len(right_list)
    for i in range(Ll + Rl):
        if Li < Ll and Ri < Rl:
            if left_list[Li] <= right_list[Ri]:
                sorted_list.append(left_list[Li])
                Li += 1
                count2+=1
            else:
                sorted_list.append(right_list[Ri])
                Ri += 1
                count2+=1
        elif Li == Ll:
            sorted_list.append(right_list[Ri])
            Ri += 1
            count2+=1
        elif Ri == Rl:
            sorted_list.append(left_list[Li])
            Li += 1
            count2+=1
    return sorted_list

def merge_sort(nums):  
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    count2+=1
    return merge(left_list, right_list)

n=int(input())
A=[randint(0,10) for i in range(n)]
quick_sort(A)
print("Среднее количество процедур 'Быстрым': ",middle(count,n))
print("Среднее количество процедур 'Слиянием': ",middle(count2,n))

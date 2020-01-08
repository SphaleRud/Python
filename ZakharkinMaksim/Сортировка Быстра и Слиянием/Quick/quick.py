def partition(n, l, h):  
    T = n[(l + h) // 2]
    i = l - 1
    j = h + 1
    while True:
        i += 1
        while n[i] < T:
            i += 1
        j -= 1
        while n[j] > T:
            j -= 1
        if i >= j:
            return j
        n[i], n[j] = n[j], n[i]

def quick_sort(n):  
    def quick_sort2(i, l, h):
        if l < h:
            split = partition(i, l, h)
            quick_sort2(i, l, split)
            quick_sort2(i, split + 1, h)
    quick_sort2(n, 0, len(n) - 1)

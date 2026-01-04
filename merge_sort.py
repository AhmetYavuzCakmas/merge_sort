def merge_two_sorted_arrays(one,two):
    sorted_list = []
    i = j = 0
    while i < len(one) and j < len(two):
        if one[i] < two[j]:
            sorted_list.append(one[i])
            i += 1
        else:
            sorted_list.append(two[j])
            j +=1

    while i <len(one):
        sorted_list.append(one[i])
        i +=1

    while j < len(two):
        sorted_list.append(two[j])
        j += 1
    return sorted_list

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr) // 2
    fh = merge_sort(arr[:mid])
    sh = merge_sort(arr[mid:])

    return merge_two_sorted_arrays(fh,sh)

arr = [70,50,30,10,20,40,60]
merged = merge_sort(arr)
print(*merged)
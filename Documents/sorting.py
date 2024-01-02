def is_sorted(lyst):
    i = 0
    j = 0
    curr = lyst[0]
    for i in range(1, len(lyst)):
        if(isinstance(lyst[i], str)):
            raise TypeError('String found, ints only')
            return(False)
        if(lyst[i - 1] > lyst[i]):
            print('unsorted')
            return(False)
        
    print('sorted')
    return(True)
    
def partition(ary, low, high):
    '''
    returns number of comparison and number of swap for current partition
    '''
    p_indx = low + (high - low) // 2
    pivot = ary[p_indx]
    done = False
    count_comp = 0
    count_swap = 0

    while not done:
        while low <= high and ary[low] < pivot:
            low += 1
            count_comp += 1

        while low <= high and ary[high] > pivot:
            high -= 1
            count_comp += 1

        if low >= high:
            done = True
        else:
            ary[low], ary[high] = ary[high], ary[low]  
            low += 1
            high -= 1
            count_swap += 1

    return high, count_comp, count_swap
    
def quick_sort(lyst, start = 0, end = -1):
    if end == -1:
        end = len(lyst) - 1
    if end <= start:
        return 0, 0

    high, cur_count_comp, cur_count_swap = partition(lyst, start, end)
    
    left_count_comp, left_count_swap = quick_sort(lyst, start, high)
    right_count_comp, right_count_swap = quick_sort(lyst, high + 1, end)

    total_count_comp = cur_count_comp + left_count_comp + right_count_comp
    total_count_swap = cur_count_swap + left_count_swap + right_count_swap

    return(total_count_comp, total_count_swap)
    
def quicksort(lyst, start = 0, end = 0):
    count, swap = quick_sort(lyst)
    return (lyst, count, swap)

def selection_sort(lyst):
    i = 0
    j = 0
    temp = lyst[0]
    count = 0
    swaps = 0
    while(i < len(lyst)):
        small_index = i
        j = i + 1
        while(j < len(lyst)):
            if(lyst[j] < lyst[small_index]):
                small_index = j
                swaps += 1
                
            j += 1
            count += 1
        
        temp = lyst[i]
        lyst[i] = lyst[small_index]
        lyst[small_index] = temp
        i += 1
    return(lyst, count, swaps)
    
def insertion_sort(lyst):
    i = 1
    j = 0
    temp = 0
    count = 0
    swaps = 0
    while(i < len(lyst)):
        j = i
        while(j > 0 and lyst[j] < lyst[j - 1]):
            temp = lyst[j]
            lyst[j] = lyst[j - 1]
            lyst[j - 1] = temp
            j -= 1
            swaps += 1
        
        count += 1
        i += 1
    return (lyst, count, swaps)
    
def merge(ary, start, mid, end):
    num_comps = 0
    num_swaps = 0
    left = ary[start:mid+1]
    right = ary[mid+1:end+1]
    indx_left = indx_right = 0
    indx_merge = start  
    
    while indx_left < len(left) and indx_right < len(right):
        num_comps += 1
        if left[indx_left] <= right[indx_right]:
            ary[indx_merge] = left[indx_left]
            indx_left += 1
        else:
            ary[indx_merge] = right[indx_right]
            indx_right += 1
        indx_merge += 1 
        num_swaps += 1   

    while indx_left < len(left):
        ary[indx_merge] = left[indx_left]
        indx_left += 1
        indx_merge += 1
        num_swaps += 1  

    while indx_right < len(right):
        ary[indx_merge] = right[indx_right]
        indx_right += 1
        indx_merge += 1
        num_swaps += 1  

    return num_comps, num_swaps 


def merge_sort(ary, start, end):
    if end <= start:
        return 0, 0
    
    mid = start + (end - start) // 2
    left_comps, left_swaps = merge_sort(ary, start, mid)
    right_comps, right_swaps = merge_sort(ary, mid + 1, end)

    merge_comps, merge_swaps = merge(ary, start, mid, end)

    total_comps = left_comps + right_comps + merge_comps
    total_swaps = left_swaps + right_swaps + merge_swaps

    return total_comps, total_swaps
    
def mergesort(lyst):
    start = 0
    end = len(lyst)-1
    count, swaps = merge_sort(lyst, start, end);
    return (lyst, count, swaps)

def main():
    pass
    

if __name__ == "__main__":
    test = [700, 302, 400, 293, 498, 291, 453, 753, 23, 346]
    mergesort(test)
    print(test)
    is_sorted(test)
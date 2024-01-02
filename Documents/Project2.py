from random import seed, sample

def make_data(data_size):#DO NOT REMOVE OR MODIFY THIS FUNCTION
    '''A generator for producing data_size random values
    '''
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()
    while True:
        yield data

def linear_search(lyst, target):
    count = 1
    print(target)
    for x in lyst:
        if x == target:
            print(count)
            return True
        else:
            count = count + 1

    return False

def binary_search(lyst, target):
    mid = 0
    low = 0
    high = len(lyst) - 1
    count = 1
    result = False
    
    while (high >= low):
        mid = int((high + low) / 2)
        if (lyst[mid] < target):
            count = count + 1
            low = mid + 1
        elif (lyst[mid] > target):
            count = count + 1
            high = mid - 1
        elif (lyst[mid] == target):
            result = True
            break
            
    return result
            
def jump_search(lyst, target):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
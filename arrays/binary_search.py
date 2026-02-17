#Exemplo de uso de binary search


def binary_search(nums, n, lo=0, hi=None):
    lo = 0
    hi = len(nums)
    steps = 0
    if hi is None:
        hi = len(nums) - 1
    while lo < hi:
        steps +=1
        mid = int((lo+hi)/2)

        if nums[mid] == n:
            print(steps)
            return mid

        elif nums[mid] < n:
            lo = mid + 1
        
        else:
            hi = mid
        
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr) 
    i = 1 # ponteiro direito indice 1 do array

    while i < n and arr[i] < target: #itera e dobra os indices até chegar no target
        i *= 2

    if arr[i] == target:
        return i
    
    return binary_search(arr, target, i//2, min(i, n-1)) # faz o min entre o 1 e o tam do array para caso o i tenha passado do tamanho do array


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
target = 16
result = exponential_search(arr, target)

print(f"Element found at index {result}")


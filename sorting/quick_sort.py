def quicksort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i] # anda com o j até encontrar um que seja menor ou igual o pivo e troca i por j
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr


test_array = [10, 7, 8, 9, 1, 5]
print("Unsorted array:", test_array)
sorted_array = quicksort(test_array)
print("Sorted array:", sorted_array)

import random as rd
def kthlowest(arr, left, right, k):
    pivot_idx = rd.randint(left, right)
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    store = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[store], arr[i] = arr[i], arr[store]
            store += 1
    arr[store], arr[right] = arr[right], arr[store]
    if store == k:
        return arr[store]
    if store < k:
        return kthlowest(arr, store + 1, right, k)
    if store > k:
        return kthlowest(arr, left, store - 1, k)
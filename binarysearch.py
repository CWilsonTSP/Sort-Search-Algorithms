# Binary Search

def search(find,arr,s,e):
    # s/e represent the start/end point
    # for each iteration
    while s <= e:
        mid = s + (e - s) // 2

        if arr[mid] == find:
            return mid

        elif arr[mid] < find:
            s = mid + 1
        else:
            e = mid - 1

    return -1 # did not find the item

items = [3, 5, 7, 12, 14, 27, 42]

x = search(12, items, 0, len(items)-1)

print(x)



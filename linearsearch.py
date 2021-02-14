# Linear Search

def search(find,arr):
    for i in range(len(arr)):
        if arr[i] == find:
            return i
    return -1 # did not find the item

items = [14, 27, 5, 3, 12, 42, 7]

x = search(12, items)

print(x)



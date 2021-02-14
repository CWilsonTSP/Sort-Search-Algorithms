# Insertion Sort

items = [14, 27, 5, 3, 12, 42, 7]

print(items)

for i in range(1, len(items)):
    key = items[i]

    j = i - 1
    while j >= 0 and key < items[j]:
        items[j+1] = items[j]
        j -= 1
    items[j+1] = key

print(items)

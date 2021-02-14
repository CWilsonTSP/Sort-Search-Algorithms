# Bubble Sort

items = [14, 27, 5, 3, 12, 42, 7]

print(items)

for i in range(len(items)):
    for j in range(0,len(items)-1):
        if items[j] > items[j+1]:
            # Swap items
            items[j], items[j+1] = items[j+1], items[j]

print(items)



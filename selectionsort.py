# Selection Sort

items = [14, 27, 5, 3, 12, 42, 7]

print(items)

for i in range(len(items)):
    mini = i
    for j in range(i+1,len(items)):
        if items[mini] > items[j]:
            mini = j
        
    # Swap items
    items[i], items[mini] = items[mini], items[i]

print(items)

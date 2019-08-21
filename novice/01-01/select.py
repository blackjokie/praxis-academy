def selection(a):
    iterasi = 0
    for i in range(len(a) - 1):
        minimal = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minimal]:
                minimal = j
        iterasi += 1
        a[minimal], a[i] = a[i], a[minimal]
        print(iterasi, a)

print ("Sorted array: ")
a=[54,26,93,17,77,31,44,55,20,21,34,65,70]
selection(a)
def bubblesort(a):
    iterasi = 0
    for j in range(len(a) - 1): #model biasa
        for i in range(len(a) - 1 - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        iterasi += 1
        print(iterasi, a)
 
print ("Sorted array: ")
a = [1,5,2,35,7,3,4]
bubblesort(a)
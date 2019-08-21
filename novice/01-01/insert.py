def insertionsort(a):
    for j in range(len(a) - 1, - 1, - 1):
        value = a[j]
        hole = j
        while hole < (len(a) - 1) and a[hole+1] > a[hole]:
            a[hole] = a[hole + 1]
            hole = hole + 1
            a[hole] = value
        print(a)

print ("Sorted array: ")
a = [3,45,34,151,34,54,76,59]
insertionsort(a)
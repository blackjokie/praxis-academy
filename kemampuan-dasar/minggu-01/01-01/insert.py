def insertionsort(a):
    for j in range(len(a)-1,-1,-1):
        value = a[j]
        hole = j
        while hole<(len(a)-1) and a[hole+1]>a[hole]:
            a[hole] = a[hole+1]
            hole = hole+1
            a[hole] = value
        print(a)
a = [1,5,2,35,7,3,4]
insertionsort(a)
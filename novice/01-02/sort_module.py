def bubblesort(a):
    iterasi = 0
    for j in range(len(a) - 1): #model biasa
        for i in range(len(a) - 1 - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        iterasi += 1
        print(iterasi, a)

def insertionsort(a):
    for j in range(len(a) - 1, - 1, - 1):
        value = a[j]
        hole = j
        while hole < (len(a) - 1) and a[hole+1] > a[hole]:
            a[hole] = a[hole + 1]
            hole = hole + 1
            a[hole] = value
        print(a)

def mergeSort(a):  
   print("Splitting ", a)
   if len(a) > 1:
       mid = len(a) // 2
       lefthalf = a[:mid]
       righthalf = a[mid:]
       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)
       i = 0
       j = 0
       k = 0
       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               a[k] = lefthalf[i]
               i = i + 1
           else:
               a[k] = righthalf[j]
               j = j + 1
           k = k + 1
       while i < len(lefthalf):
           a[k] = lefthalf[i]
           i = i + 1
           k = k + 1
       while j < len(righthalf):
           a[k]=righthalf[j]
           j = j + 1
           k = k + 1
   print("Merging ", a)
    
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
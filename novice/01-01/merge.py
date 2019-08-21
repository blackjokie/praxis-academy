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
a = [1,5,2,35,7,3,4]
mergeSort(a)
print(a)
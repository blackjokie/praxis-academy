def bubblesort(alist):
    iterasi = 0
    for j in range(len(alist)-1): #model biasa
        for i in range(len(alist)-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
        iterasi+=1
        print(iterasi,alist)
 
alist = [1,5,2,35,7,3,4]
bubblesort(alist)
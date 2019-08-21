# mengambil function - function yang akan digunakan pada modul ini
from sort_module import bubblesort, insertionsort, mergeSort, selection
from quick_module import quickshort, partition

# a = [1,5,2,35,7,3,4]
try:
    a = input("Masukkan angka yang hendak di sort (dipisahkan spasi): ")
    list  = a.split()
    b = input("Pilih metode sort (bubble, insert, quick, merge, select): ")

    if b == "bubble":
        # memanggil function "bubblesort" pada module "sort_module" dan menjalankan operasi dengan input "list" 
        print ("Sorted array: ")
        bubblesort(list)
    elif b == "insert":
        # memanggil function "insertionsort" pada module "sort_module" dan menjalankan operasi dengan input "list"
        print ("Sorted array: ")
        insertionsort(list)
    elif b == "quick":
        # memanggil function "quickshort", "partition" pada module "quick_module" dan menjalankan operasi dengan input "list"
        print ("Sorted array: ")
        quickshort(list, 0, len(list) - 1)
    elif b == "merge":
        # memanggil function "mergeSort" pada module "sort_module dan menjalankan operasi dengan input "list"
        print ("Sorted array: ")
        mergeSort(list)
        print(list)
    else:
        # memanggil fungsi "selection" pada module "sort_module dan menjalankan operasi dengan input "list"
        print ("Sorted array: ")
        selection(list)

except (KeyboardInterrupt, SystemExit):
    print("\nTerimakasih !")


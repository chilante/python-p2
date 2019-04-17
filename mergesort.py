## Henrique Nóbrega Grigolli - 41821661
## Carlos Henrique Chilante - 31898416
def MergeSort(A):
    n = len(A)
    left = A[:n//2]
    right = A[n//2:]
    if(n > 1):
        meio = n//2
        for i in range(0,meio):
            left[i] = A[i]
        for i in range(meio, n-1):
            right[i-meio] = A[i]

        MergeSort(left)
        MergeSort(right)
        merge(A, left, right)
        print(A)


def merge(A, left, right):
    nL = len(left)
    nR = len(right)
    i = 0
    j = 0
    k = 0

    while(i < nL and j < nR):
        if(left[i] <= right[j]):
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while (i < nL):
        A[k] = left[i]
        i += 1
        k += 1
    while (j< nR):
        A[k] = right[j]
        j += 1
        k += 1        


A = [1,4,2,3, 6,7,8,88,9]

MergeSort(A)

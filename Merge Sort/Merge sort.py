def MergeSort(a,p=0,r=None):
    if r is None:
        r = len(a) - 1
    if p < r:
        q = (p + r) // 2
        MergeSort(a,p,q)
        MergeSort(a,q + 1,r)
        Merge(a,p,q,r)

def Merge(a,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(1,n1 + 1):
        L[i - 1] = a[p + i -1]
    for j in range(1,n2 + 1):
        R[j - 1] = a[q + j]
    L[-1] = float('inf')
    R[-1] = float('inf')
    i = 0
    j = 0
    for k in range(p,r + 1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1

if __name__ == "__main__":
    import numpy as np
    a = np.random.normal(1,1,216)
    MergeSort(a)
    print(a)
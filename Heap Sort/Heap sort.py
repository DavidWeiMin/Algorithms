def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def heapify(a,i,heapSize):
    l = left(i)
    r = right(i)
    if l <= heapSize and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[largest],a[i] = a[i],a[largest]
        heapify(a,largest,heapSize)

def buildMaxHeap(a):
    for i in range((len(a) - 1) // 2,-1,-1):
        heapify(a,i,len(a) - 1)

def heapsort(a):
    buildMaxHeap(a)
    for i in range(len(a) - 1,0,-1):
        a[0],a[i] = a[i],a[0]
        heapify(a,0,i - 1)
    return a

if __name__ == "__main__":
    import numpy as np
    a = np.random.randint(1,2000,100)
    a = heapsort(a)
    print(a)
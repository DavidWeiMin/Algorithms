def maximum_subarrray(a,low,high):
    if low == high:
        return low,high,a[low]
    mid = (low + high) // 2
    left_low,left_high,left_sum = maximum_subarrray(a,low,mid)
    right_low,right_high,right_sum = maximum_subarrray(a,mid + 1,high)
    cross_low,cross_high,cross_sum = cross(a,low,high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low,left_high,left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low,right_high,right_sum
    else:
        return cross_low,cross_high,cross_sum

def cross(a,low,high):
    mid  = (low + high) // 2
    left_sum = - float('inf')
    summation = 0
    for i in range(mid,low - 1,-1):
        summation += a[i]
        if summation > left_sum:
            left_sum = summation
            max_left = i
    right_sum = -float('inf')
    summation = 0
    for j in range(mid + 1,high + 1):
        summation += a[j]
        if summation > right_sum:
            right_sum = summation
            max_right = j
    return max_left,max_right,left_sum + right_sum

def transform(a):
    b = []
    for i in range(len(a) - 1):
        b.append(a[i + 1] - a[i])
    return b

if __name__ == "__main__":
    import numpy as np
    a = list(np.random.randint(1,20,30))
    print(a)
    a = transform(a)
    print(a)
    print(maximum_subarrray(a,0,len(a) - 1))
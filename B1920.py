# 수 찾기
# Binary Search 문제

def binarySearch(low, high, a, key):
    while True:
        mid = (low + high) // 2
        if a[mid] == key:
            print('1')
            break
        elif low > high:
            print('0')
            break
        else:
            if a[mid] > key:
                high = mid - 1
            elif a[mid] < key:
                low = mid + 1

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
m = int(input())
b = [int(x) for x in input().split()]

for i in range(m):
    binarySearch(0, n - 1, a, b[i])



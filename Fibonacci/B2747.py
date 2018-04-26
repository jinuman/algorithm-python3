# 피보나치 수

def fibonacci(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, 46):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]

print(fibonacci(int(input())))

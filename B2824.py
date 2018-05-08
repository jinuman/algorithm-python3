# 최대공약수

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]
aMul = 1
bMul = 1
for item in a:
    aMul *= item
for item in b:
    bMul *= item
result = gcd(aMul, bMul)
if len(str(result)) >= 9:
    start = len(str(result)) - 9
    print(str(result)[start:])
else:
    print(result)
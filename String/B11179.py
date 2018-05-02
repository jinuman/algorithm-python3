# 2진수 뒤집기
# int(str, 2) --> 2진수의 str을 10진수로 변환
# bin(int) --> int to 2진수(str)

print(int(bin(int(input()))[2:][::-1], 2))
# 알파벳 개수
'''
알파벳 소문자로만 이루어진 단어 s
각 알파벳이 몇개가 포함되어 있는지 구하는 문제
a의 개수, b의 개수, .... , z의 개수

ASCII Code !!
chr() : int to char
ord() : char to int ex) ord("z") = 122
'''
s = input()
for i in range(97, 123):
    print(s.count(chr(i)), end=" ")
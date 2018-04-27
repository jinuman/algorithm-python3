# 알파벳 찾기
'''
문자열에서 각 알파벳이 몇번째에 처음 등장하는지 구하는 문제
find 함수 사용
'''
s = input()
for i in range(97, 123):
    print(s.find(chr(i)), end=" ")
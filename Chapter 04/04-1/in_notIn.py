# 리스트 내부에 있는지 확인하기: in/not in 연산자

list_a = [273,32,103,57,52]

# in 연산자
print("# in 연산자")
print(273 in list_a)
print(99 in list_a)
print(52 in list_a)
print()

# not in 연산자
print("# not in 연산자")
print(273 not in list_a)
print(99 not in list_a)
print(52 not in list_a)

# 출력값
"""
# in 연산자
True
False
True

# not in 연산자
False
True
False
"""

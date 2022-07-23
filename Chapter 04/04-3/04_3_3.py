# 확인문제 3

limit = 10000
i = 1

# sum은 파이썬 내부에서 사용하는 식별자이므로 sum_value라는 변수 이름을 사용한다.
sum_value = 0

while sum_value <= limit:
    sum_value += i
    i += 1
print("{}를 더할 떄 {}을 넘으며 그떄의 값은 {}이다.".format(i-1, limit, sum_value))

# 출력값
"""
141를 더할 떄 10000을 넘으며 그떄의 값은 10011이다.
"""
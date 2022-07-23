# 확인문제 4
# 1부터 100까지의 숫자가 있을 때 최대가 되는 경우

max_value = 0
a= 0
b= 0

for i in range(0,100//2 +1):
    j = 100 -i

    # 최대값 구하기
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current

print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))

# 출력값
"""
최대가 되는 경우 : 50 * 50 = 2500
"""
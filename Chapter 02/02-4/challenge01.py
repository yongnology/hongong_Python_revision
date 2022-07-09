# 1. 구의 부피와 겉넓이

import math


r = float(input("구의 반지름을 입력해주세요: "))

bupi = float(4/3*(math.pi)*r*r*r)   # (4/3) * math.pi * (r**3)
gut = float(4*math.pi*r*r)          # 4 * math.pi * (r**2)

print(f"= 구의 부피는 {bupi} 입니다.")
print(f"= 구의 겉넓이는 {gut} 입니다.")

# 출력값
"""
구의 반지름을 입력해주세요: 5
= 구의 부피는  523.5987755982989 입니다.
= 구의 겉넓이는  314.1592653589793 입니다.
"""

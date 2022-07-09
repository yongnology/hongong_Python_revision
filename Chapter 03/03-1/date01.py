# 날짜/시간을 한 줄로 출력하기

# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print("{}년 {}월 {}일 {}시 {}분 {}초". format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 출력값
"""
2022년 7월 9일 23시 20분 58초
"""
# 다른 프로그래밍 언어와 다르게 달을 그대로 출력한다.
# 0부터 시작이 아닌 1부터 시작해서 출력한다.

# 계절을 구분하는 프로그램

# 날짜/시간과 관련되 기능을 가져옵니다.
import datetime

# 현재 날짜//시간을 구한다.
now = datetime.datetime.now()

# 봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

# 여름 구분
if 6 <= now.month <=8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))

# 가을 구분
if 9 <= now.month <=11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))

# 겨울 구분
if now.month == 12 or 1 <= now.month <=2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))

# 출력값
"""
이번 달은 7월로 여름입니다.
"""

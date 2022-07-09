# 도전문제
# 1. 간단한 대화 프로그램

import datetime

입력 = input("입력: ")

if "안녕" in 입력:
    print("안녕하세요.")

elif "몇 시" in 입력:
    now = datetime.datetime.now()
    print(f"지금은 {now.hour}시 입니다.")
else:
    print(입력)

# 출력값
"""
입력: 안녕!!
안녕하세요.

입력: 지금 몇 시 야?
지금은 1시 입니다.
"""

# inch 단위를 cm 단위로 변경하기

# 숫자를 입력받습니다.
raw_input = input("inch 단위의 숫자를 입력해주세요: ")

# 입력받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
inch = int(raw_input)
cm = inch * 2.54

# 출력합니다.
print(inch, "inch는 cm 단위로", cm, "cm입니다.")

# 출력값
"""
inch 단위의 숫자를 입력해주세요: 27
27 inch는 cm 단위로 68.58 cm입니다.
"""
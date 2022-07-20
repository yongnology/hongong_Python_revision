# 키가 존재하는지 확인하고 값에 접근하기

# 딕셔너리를 선언한다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 사용자로부터 입력을 받는다.
key = input(">접근하고자 하는 키:")

# 출력한다.
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# 출력값
"""
>접근하고자 하는 키:10
존재하지 않는 키에 접근하고 있습니다.

>접근하고자 하는 키:name
7D 건조 망고
"""
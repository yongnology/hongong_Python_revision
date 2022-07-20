# 키가 존재하지 않을 때 None을 출력하는지 확인하기

# 딕셔너리를 선언한다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 존재하지 않는 키에 접근한다.
value = dictionary.get("존재하지 않는 키")
print("값", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")

# 출력값
"""
값 None
존재하지 않는 키에 접근했었습니다.
"""
# 딕셔너리를 선언한다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

# 요소 제거 전에 내용을 출력한다.
print("요소 제거 이전:", dictionary)

# 딕셔너리의 요소를 제거한다.
del dictionary["name"]
del dictionary["type"]

# 요소 제거 후 내용을 출력
print("요소 제거 이후:",dictionary)

# 출력값
"""
요소 제거 이전: {'name': '7D 건조 망고', 'type': '당절임'}
요소 제거 이후: {}
"""
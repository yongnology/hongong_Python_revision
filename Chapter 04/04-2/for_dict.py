# for 반복문 딕셔너리

# 딕셔너리를 선언한다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# for 반복문을 사용한다.
for key in dictionary:
    # 출력한다.
    print(key, ":", dictionary[key])

# 출력값
"""
name : 7D 건조 망고
type : 당절임
ingredient : ['망고', '설탕', '메타중아황산나트륨', '치자황색소']
origin : 필리핀
"""
# 확인 4

# 딕셔너리를 선언한다.
character = {
    "name": "기사",
    "level":12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill":["배기", "세게 베기", "아주 세게 베기"]
}

# for 반복문을 사용한다.
for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":", character[key])

# 출력값
"""
name : 기사
level : 12
sword : 불꽃의 검
armor : 풀플레이트
skill : 배기
skill : 세게 베기
skill : 아주 세게 베기
"""
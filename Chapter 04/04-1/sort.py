# 리스트 정렬하기: sort()

list_e = [52, 273, 103, 32, 275, 1, 7]
list_e.sort()   # 오름차순

print("sort()", list_e)
print()

list_e.sort(reverse=True)
print("sort(reverse=True)", list_e)

# 출력값
"""
sort() [1, 7, 32, 52, 103, 273, 275]

sort(reverse=True) [275, 273, 103, 52, 32, 7, 1]
"""

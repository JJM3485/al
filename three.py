import random

def ternary_search(arr, target, low, high):
    if low > high:
        return -1  # 아이템이 없음

    third = (high - low) // 3
    first_third = low + third
    second_third = high - third

    if arr[first_third] == target:
        return first_third
    if arr[second_third] == target:
        return second_third

    if target < arr[first_third]:
        return ternary_search(arr, target, low, first_third - 1)
    elif target > arr[second_third]:
        return ternary_search(arr, target, second_third + 1, high)
    else:
        return ternary_search(arr, target, first_third + 1, second_third - 1)

# 배열 생성 및 정렬
n = 20
s = [random.randint(0, n) for _ in range(n)]
s.sort()
print("정렬된 리스트:", s)

# 찾을 타겟 값도 랜덤으로 설정
target = random.choice(s)
print("찾을 값:", target)

# 탐색 실행
result = ternary_search(s, target, 0, len(s) - 1)

# 결과 출력
print(f"찾은 인덱스: {result}" if result != -1 else "아이템이 리스트에 없습니다.")

import random
import time

def three_search(arr, target, low, high):
    if low > high:
        return -1  # 아이템이 없음

    third = (high - low) // 3  # 3등분으로 나누기
    first_third = low + third  # 첫번째 부분 
    second_third = high - third  # 두번째 부분

    if arr[first_third] == target:  # 나누는 기준이 찾는 값일 경우
        return first_third
    if arr[second_third] == target:  # 나누는 기준이 찾는 값일 경우
        return second_third

    if target < arr[first_third]:  # 첫 부분 기준보다 찾는 값이 작을 경우
        return three_search(arr, target, low, first_third - 1)
    elif target > arr[second_third]:  # 두번째 부분 기준보다 찾는 값이 큰 경우
        return three_search(arr, target, second_third + 1, high)
    else:  # 가운데 부분에 있을 경우
        return three_search(arr, target, first_third + 1, second_third - 1)

# 배열 생성 및 정렬
n = 1000000
s = [random.randint(0, n) for _ in range(n)]
s.sort()
print("정렬된 리스트:", s)

# 찾을 타겟 값도 랜덤으로 설정
target = random.choice(s)
print("찾을 값:", target)

#수행 시간 시작
start = time.time()

# 검색 실행
result = three_search(s, target, 0, len(s) - 1)

#수행 시간 끝
end = time.time()

# 결과 출력
print(f"찾은 인덱스: {result}" if result != -1 else "아이템이 리스트에 없습니다.")
print(f"수행 시간: {end - start:.10f}초")

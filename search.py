import random
import time


def main():
    num = 1000000 #리스트의 크기
    s = [] # 리스트

    for value in range(num): #값을 추가
        s.append(random.randint(0, num))

    key = random.randint(0, num) #찾고자 하는 값

    start = time.perf_counter() #시작 시간
    location = sequential_search(s, key) #순차 탐색
    end = time.perf_counter() #종료 시간

    #print(s)
    print("[Sequential Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print()

    s.sort() # 정렬을 위한 코드

    start = time.perf_counter() #시작 시간
    location = binary_search(s, key) #이진 탐색
    end = time.perf_counter() #종료 시간

    #print(s)
    print("[Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print()

    start = time.perf_counter() #시작 시간
    location = recursive_binary_search(s, key, 0, num - 1) #재귀 이진 탐색
    end = time.perf_counter() #종료 시간

    #print(s)
    print("[Recursive Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print()


def sequential_search(s, key):
    num = len(s)
    location = 0
    for i in range(num): # 리스트의 크기만큼 반복
        if s[i] == key: # 키를 발견할 경우
            return i  # 키 값이 발견된 위치 반환
    return -1  # 찾지 못했을 경우 -1 반환


def binary_search(s, key):
    num = len(s)
    low = 0
    high = num - 1
    location = -1

    while low <= high:
        mid = (low + high) // 2  # 중간 위치 계산
        if s[mid] == key:
            return mid  # 키 값 발견
        elif s[mid] < key:
            low = mid + 1  # 오른쪽 부분 탐색
        else:
            high = mid - 1  # 왼쪽 부분 탐색
    
    return -1  # 찾지 못했을 경우 -1 반환


def recursive_binary_search(s, key, low, high):
    mid = round((low + high) / 2) #중간값 입력

    if low > high:
        return -1  # 탐색 실패 시 -1 반환
    if s[mid] == key:
        return mid  # 키 값 발견
    elif s[mid] < key:
        return recursive_binary_search(s, key, mid + 1, high)  # 중간을 기준으로 오른쪽 부분 탐색
    else:
        return recursive_binary_search(s, key, low, mid - 1)  # 중간을 기준으로 왼쪽 부분 탐색


if __name__ == "__main__":
    main()

import random
import time

def main():
    ###################
    #   Create List   #
    ###################

    n = 100
    s = [random.randint(0, n) for _ in range(n)]
    
    s1 = s.copy()
    s2 = s.copy()
    s.sort()

    ##################
    #   Merge Sort   #
    ##################

    start = time.perf_counter()
    merge_sort(s=s1, low=0, high=len(s1) - 1)
    end = time.perf_counter()
    print("[Merge Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print("Correct:", s == s1)
    print()

    ##################
    #   Quick Sort   #
    ##################

    start = time.perf_counter()
    quick_sort(s=s2, low=0, high=len(s2) - 1)
    end = time.perf_counter()
    print("[Quick Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print("Correct:", s == s2)
    print()

    #############
    #   TRIAL   #
    #############

    TRIAL = 100
    total_elapsed_time_merge_sort = 0
    total_elapsed_time_quick_sort = 0

    print("[progressing] - TRIAL: {}".format(TRIAL))
    print(">" * (TRIAL // (TRIAL // 20)))

    for trial in range(TRIAL):
        # Create list
        n = 5000
        s = [random.randint(0, n) for _ in range(n)]
        
        s1 = s.copy()
        s2 = s.copy()

        # Merge Sort
        start = time.perf_counter()
        merge_sort(s=s1, low=0, high=len(s1) - 1)
        end = time.perf_counter()
        total_elapsed_time_merge_sort += end - start

        # Quick Sort
        start = time.perf_counter()
        quick_sort(s=s2, low=0, high=len(s2) - 1)
        end = time.perf_counter()
        total_elapsed_time_quick_sort += end - start

        if TRIAL >= 20 and (trial + 1) % (TRIAL // 20) == 0:
            print(">", end="", flush=True)

    print()
    print("Merge Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_merge_sort))
    print("Quick Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_quick_sort))

def merge_sort(s, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(s, low, mid)
        merge_sort(s, mid + 1, high)
        merge(s, low, mid, high)

def merge(s, low, mid, high):
    left = s[low:mid + 1]  # 왼쪽 부분 배열
    right = s[mid + 1:high + 1]  # 오른쪽 부분 배열
    i = j = 0  # 각 부분 배열의 인덱스
    k = low  # 원래 배열의 인덱스
    
    # 두 배열을 비교하며 정렬
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            s[k] = left[i]
            i += 1
        else:
            s[k] = right[j]
            j += 1
        k += 1
    
    # 남은 요소들 추가
    while i < len(left):
        s[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        s[k] = right[j]
        j += 1
        k += 1

def quick_sort(s, low, high):
    if low < high:
        pivot = partition(s, low, high)
        quick_sort(s, low, pivot - 1)
        quick_sort(s, pivot + 1, high)

def partition(s, low, high):
    pivot = s[high]  # 피벗 요소 선택
    i = low - 1  # 피벗보다 작은 요소들의 위치
    
    for j in range(low, high):
        if s[j] <= pivot:  # 현재 요소가 피벗 이하라면
            i += 1
            s[i], s[j] = s[j], s[i]  # 자리 교환
    
    s[i + 1], s[high] = s[high], s[i + 1]  # 피벗을 올바른 위치로 이동
    return i + 1  # 새로운 피벗의 인덱스 반환

if __name__ == "__main__":
    main()
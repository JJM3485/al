def percolate_down(A, k, n):
    """
    A[k]를 루트로 하는 서브 트리가 A[k...n-1] 범위 내에서 힙 성질을 만족하도록 수선한다.
    주어진 조건: A[k]의 두 자식을 루트로 하는 서브 트리는 힙 특성을 만족한다.
    """
    child = 2 * k + 1  # 왼쪽 자식
    right = 2 * k + 2  # 오른쪽 자식


    # 코딩을 추가하세요.




def build_heap(A):
    """배열 A[0...n-1]을 힙으로 만든다."""
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):  # (n-2)/2 downto 0
        percolate_down(A, i, n)




def delete_max(A):
    """힙 A[0...n-1]에서 최댓값을 알려주며 삭제한다."""
    n = len(A)
    max_val = A[0]
    A[0] = A[n - 1]


    # 코딩을 추가하세요.


    return max_val




def heap_sort(A):
    """배열 A[0...n-1]을 정렬한다."""
    result = A.copy()  # 원본 배열을 보존하기 위해 복사
    build_heap(result)
    sorted_array = []


    for i in range(len(A) - 1, 0, -1):  # n-1 downto 1
        # deleteMax의 결과를 sorted_array에 추가
        sorted_array.append(delete_max(result))


    # 마지막 원소 추가 (힙에 하나만 남았을 때)
    if result:
        sorted_array.append(result[0])


    return sorted_array




# 테스트
if __name__ == "__main__":
    # 테스트 배열
    test_array = [4, 10, 3, 5, 1, 21, 17, 9]
    print("원본 배열:", test_array)


    # 힙 정렬 수행
    sorted_array = heap_sort(test_array)
    print("정렬된 배열:", sorted_array)

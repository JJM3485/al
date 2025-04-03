import random

def percolate_down(A, k, n):
    """
    A[k]를 루트로 하는 서브 트리가 A[k...n-1] 범위 내에서 힙 성질을 만족하도록 수선한다.
    주어진 조건: A[k]의 두 자식을 루트로 하는 서브 트리는 힙 특성을 만족한다.
    """
    child = 2 * k + 1  # 왼쪽 자식
    while child < n:
        right = child + 1  # 오른쪽 자식
        
        # 오른쪽 자식이 있고, 오른쪽 자식이 왼쪽 자식보다 크다면 오른쪽 자식을 선택
        if right < n and A[right] > A[child]:
            child = right
        
        # 현재 노드가 자식보다 크다면 종료
        if A[k] >= A[child]:
            break
        
        # 교환
        A[k], A[child] = A[child], A[k]
        k = child
        child = 2 * k + 1  # 다음 왼쪽 자식 갱신

def build_heap(A):
    """배열 A[0...n-1]을 힙으로 만든다."""
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):  # (n-2)/2 downto 0
        percolate_down(A, i, n)

def delete_max(A):
    """힙 A[0...n-1]에서 최댓값을 알려주며 삭제한다."""
    n = len(A)
    if n == 0:
        return None  # 빈 힙이면 None 반환
    
    max_val = A[0]
    A[0] = A[n - 1]  # 마지막 요소를 루트로 이동
    A.pop()  # 마지막 요소 제거
    percolate_down(A, 0, len(A))  # 힙 속성 유지
    
    return max_val

def heap_sort(A):
    """배열 A[0...n-1]을 정렬한다."""
    result = A.copy()  # 원본 배열을 보존하기 위해 복사
    build_heap(result)
    sorted_array = []
    
    for _ in range(len(A)):
        sorted_array.append(delete_max(result))
    
    return sorted_array[::-1]  # 내림차순으로 정렬된 결과이므로 뒤집기

# 테스트
if __name__ == "__main__":
    # 테스트 배열
    test_array = [4, 10, 3, 5, 1, 21, 17, 9]
    print("원본 배열:", test_array)
    
    # 힙 정렬 수행
    sorted_array = heap_sort(test_array)
    print("정렬된 배열:", sorted_array)

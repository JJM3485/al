class Node:
    def __init__(self, key):
        self.key = key  # 노드의 키 값
        self.parent = None # 부모 노드
        self.left = None # 왼쪽 자식
        self.right = None # 오른쪽 자식식


    def __str__(self):
        # 노드와 부모 노드의 키를 문자열로 리턴
        return "[NODE - key: {0}, parent key: {1}]".format(self.key, self.parent.key)




class BST(object):
    def __init__(self, max_num_keys=3):
        self.root = None # 루트 노드
        self.size = 0 #노드의 수


    # 중위 순회 (Inorder traversal)
    def _inorder(self, node=None):
        if node is not None:
            # 왼쪽으로 순회
            self._inorder(node.left)


            # 중앙 노드 키 출력
            print(str(node.key), end=" ")


            # 오른쪽으로 순회
            self._inorder(node.right)


    def print_bst(self):
        self._inorder(self.root) #중위 시작
        print(": SIZE = {0}".format(self.size)) # 총 노드의 수


    # 노드 검색 (비재귀적 버전)
    def tree_search(self, key=None):
        if self.root is None:
            return None  # 트리가 비어있으면 None 반환
        else:
            current_node = self.root # 루트부터 탐색 시작
            while current_node is not None:
                if key == current_node.key:
                    return current_node # 찾는 키와 같으면 노드 반환


                if key < current_node.key:  # 작으면 왼쪽으로 크면 오른쪽으로 이동
                    current_node = current_node.left
                else:
                    current_node = current_node.right


            return None # 찾지 못한 경우


    def tree_insert(self, key=None):
        new_node = Node(key=key) # 새로운 노드 생성

        if self.root is None:  #트리가 비어 있으면 루트로 설정
            self.root = new_node
        else:
            # 새로운 노드를 위한 올바른 위치까지 순회하여 새로운 노드의 부모 설정
            current_node = self.root
            parent_node_for_new_node = None

            while current_node is not None: # 삽입 위치를 찾을 때까지 반복
                parent_node_for_new_node = current_node
                if key < current_node.key:
                    current_node = current_node.left #왼쪽으로 이동
                else:
                    current_node = current_node.right # 오른쪽으로 이동

            # 새로운 노드를 부모의 왼쪽 또는 오른쪽에 연결
            if key < parent_node_for_new_node.key:
                parent_node_for_new_node.left = new_node
            else:
                parent_node_for_new_node.right = new_node

            # 새로운 노드의 부모 노드 설정
            new_node.parent = parent_node_for_new_node

        self.size += 1 # 트리 크기 증가




    # 노드 삭제 (비재귀적 버전)
    def tree_delete(self, key):
        node_to_be_deleted = self.tree_search(key) # 삭제할 노드 검색
        if node_to_be_deleted is None:
            return # 찾지 못하면 아무 작업 안 함
        else:
            # node_to_be_deleted가 루트인 경우
            if node_to_be_deleted == self.root: 
                self.root = self._delete_node(node_to_be_deleted)
            elif node_to_be_deleted == node_to_be_deleted.parent.left: #왼쪽일 경우
                node_to_be_deleted.parent.left = self._delete_node(node_to_be_deleted)
            else: #오른쪽일 경우
                node_to_be_deleted.parent.right = self._delete_node(node_to_be_deleted)


            self.size -= 1 # 트리 크기 감소


    def _delete_node(self, node_to_be_deleted):
        if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
            return None # 자식이 없으면 그냥 삭제
        elif node_to_be_deleted.left is None and node_to_be_deleted.right is not None:
            node_to_be_deleted.right.parent = node_to_be_deleted.parent
            return node_to_be_deleted.right  # 오른쪽 자식만 있을 경우, 오른쪽 자식을 반환
        elif node_to_be_deleted.left is not None and node_to_be_deleted.right is None:
            node_to_be_deleted.left.parent = node_to_be_deleted.parent
            return node_to_be_deleted.left # 왼쪽 자식만 있을 경우, 왼쪽 자식을 반환
        else:
            # 삭제할 노드의 오른쪽 자식을 smallest_node로 설정
            smallest_node = node_to_be_deleted.right

            # 처음에는 smallest_node의 부모는 삭제할 노드 자신
            parent_of_smallest_node = None

            while smallest_node.left is not None:
                parent_of_smallest_node = smallest_node
                smallest_node = smallest_node.left # 오른쪽 서브트리의 최소 노드 찾기

            # successor의 키를 현재 노드에 복사
            node_to_be_deleted.key = smallest_node.key 

            # successor 노드 제거 (자식은 최대 하나)
            if parent_of_smallest_node is None:
                node_to_be_deleted.right = smallest_node.right
                if smallest_node.right is not None:
                    smallest_node.right.parent = node_to_be_deleted
            else:
                parent_of_smallest_node.left = smallest_node.right
                if smallest_node.right is not None:
                    smallest_node.right.parent = parent_of_smallest_node

            del smallest_node
            return node_to_be_deleted






if __name__ == "__main__":
    bst = BST()

    # 여러 키 삽입 (트리 생성)
    bst.tree_insert(8)
    bst.tree_insert(3)
    bst.tree_insert(1)
    bst.tree_insert(6)
    bst.tree_insert(7)
    bst.tree_insert(10)
    bst.tree_insert(14)
    bst.tree_insert(4)


    bst.print_bst() # 트리 출력 (중위 순회)
    print("\nSearch 10:", bst.tree_search(10))
    print("\nSearch 100:", bst.tree_search(100))


    print("\nDelete 10")
    bst.tree_delete(10)
    bst.print_bst()


    print("\nDelete 10")
    bst.tree_delete(10)
    bst.print_bst()


    print("\nDelete 3")
    bst.tree_delete(3)
    bst.print_bst()


    print("\nDelete 4")
    bst.tree_delete(4)
    bst.print_bst()


    print("\nDelete 8")
    bst.tree_delete(8)
    bst.print_bst()



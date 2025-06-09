class TreeNode:
    def __init__(self, value=0):
        self.val = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """插入節點"""
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    # _function:內部使用函式
    def _insert_recursive(self, node, val):
        """遞迴插入節點"""
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        elif val < node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)
        # 如果值相等，不插入（BST通常不允許重複值）

    def search(self, val):
        """搜尋節點"""
        return self._search_recursive(self.root, val)

    def _search_recursive(node, val):
        """遞迴搜尋節點"""
        if not node or node.val == val:
            return node
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)

    def preorder_traversal(self):
        """遍歷方式: 根 -> 右 -> 左"""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.val)  # 訪問根節點
            self._preorder_recursive(node.left, result)  # 遍歷左子樹
            self._preorder_recursive(node.right, result)  # 遍歷右子樹


# 使用範例
if __name__ == "__main__":
    # 建立BST
    bst = BST()

    # 插入節點
    values = [50, 30, 70, 20, 40, 60, 80]
    print("插入節點:", values)

    for val in values:
        bst.insert(val)

    print()
    # 三種遍歷方式
    print(f"\n前序遍歷 (根->左->右): {bst.preorder_traversal()}")

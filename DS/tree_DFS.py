# === tree節點 ===
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# === tree的簡單遍歷 ===
def traverse(root: TreeNode):
    if root is None:
        return
    traverse(root.left)
    traverse(root.right)


# 深度優先遍歷(DFS) - 遞歸實現
class TreeTraverse:

    def preorder_traversal(self, root):
        """
        前序遍歷 : 根 -> 左 -> 右
        """
        result = []

        def dfs(node):
            if node is None:
                return
            result.append(node.val)  # 訪問根節點
            dfs(node.left)  # 遍歷左子樹
            dfs(node.right)  # 遍歷右子樹

        dfs(root)
        return result

    def inorder_traversal(self, root):
        """
        中序遍歷 : 左 -> 根 -> 右
        對於二元搜尋樹，中序遍歷會得到有序序列
        常用於複製樹的結構
        """
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)  # 遍歷左子樹
            result.append(node.val)  # 訪問根節點
            dfs(node.right)  # 遍歷右子樹

        dfs(root)
        return result

    def postorder_traversal(self, root):
        """
        後序遍歷 : 左 -> 右 -> 根
        常用於刪除樹或計算樹的屬性 （如樹的高度）
        """
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)  # 遍歷左子樹
            dfs(node.right)  # 遍歷右子樹
            result.append(node.val)  # 訪問根節點

        dfs(root)
        return result


# 深度優先遍歷 - 迭代實現（使用堆疊）
class IterativeTraversal:

    def preorder_iterative(self, root):
        """
        前序遍歷的迭代實現
        """
        if not root:
            return []

        result = []
        stack = [root]
        while (
            stack
        ):  # while stack是判斷是否為空陣列 , while "string" 是判斷是不是空字串..
            node = stack.pop()
            result.append(node.val)

            # 注意:先放右子樹 再放左子樹
            # 因為stack是LIFO,所以左子樹會先被處理
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def inorder_iterative(self, root):
        """
        中序遍歷的迭代實現
        """

        result = []
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            # 處理當前節點
            current = stack.pop()
            result.append(current.val)
            # 移動到右子樹
            current = current.right
        return result


if __name__ == "__main__":

    stack = [1]
    num = 5
    while stack:
        print(stack.pop())
        if num > 0:
            stack.append(num)
            num = num - 1

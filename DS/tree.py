class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self):
        nodes = [self]
        while nodes:
            current_node = nodes.pop(0)
            print(current_node.value)
            nodes.extend(current_node.children)


root = TreeNode("Root")
child1 = TreeNode("Child1")
child2 = TreeNode("Child2")
root.add_child(child1)
root.add_child(child2)

grandchild1 = TreeNode("Grandchild1")
grandchild2 = TreeNode("Grandchild2")
child1.add_child(grandchild1)
child2.add_child(grandchild2)
child1.remove_child(grandchild1)
root.traverse()

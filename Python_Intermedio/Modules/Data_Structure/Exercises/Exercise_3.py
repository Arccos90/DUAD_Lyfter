"-------------------------------------Exercise_3_Data_structures---------------------------------"

class TreeNode:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right =None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root #nodo raiz

    def print_structure(self):
        if self.root is None:
            print ("El arbol está vacío")
            return
        self.print_recursive(self.root, parent=None)
    def print_recursive(self, node, parent = None):
        if node is None:
            return

        if parent  is None:
            print(f"Raíz (Abuela): {node.data}")
        else:
            print(f"Hijo de {parent.data}: {node.data}")
        self.print_recursive(node.left, parent=node)
        self.print_recursive(node.right, parent=node)

root = TreeNode ("Ana")
tree = BinaryTree(root)
tree.root.left = TreeNode("Daniel")
tree.root.right = TreeNode("Beatriz")
tree.root.left.right = TreeNode("Alana")
tree.root.right.left = TreeNode ("Mateo")
tree.root.right.right = TreeNode ("Javier")
tree.root.right.left.right = TreeNode("Bandit")
tree.root.left.right.right = TreeNode("Sansa")

tree.print_structure()
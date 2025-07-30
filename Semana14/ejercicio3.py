# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    
    data: str
    left: "Node"
    right: "Node"
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    root:Node
    
    def __init__(self):
        self.root = None

    def push(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.push_recursive(self.root, value)

    def push_recursive(self, current_node, value):
        if value < current_node.data:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.push_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.push_recursive(current_node.right, value)

    def print_binary_tree(self):
        self.print_structure(self.root, 0)

    def print_structure(self, node, level):
        if node is not None:
            self.print_structure(node.right, level + 1)
            print("    " * level + f"-> {node.data}")
            self.print_structure(node.left, level + 1)


structure = BinaryTree()

structure.push("M")
structure.push("C")
structure.push("R")
structure.push("A")
structure.push("D")
structure.push("Z")

structure.print_binary_tree()

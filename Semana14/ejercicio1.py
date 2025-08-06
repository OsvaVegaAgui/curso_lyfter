# 1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    top: Node

    def __init__(self):
        self.top = None
        
    def print_structure(self):
        current_node = self.top

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
            
    def push(self, value):
        current_node = Node(value,self.top)
        self.top = current_node
        
    def pop(self):
        if self.top:
            self.top = self.top.next
        else:
            print("The stack is empty, cannot perform pop.")
        
structure = Stack()

structure.push(3)
structure.push(8)
structure.push(5)
structure.push(35)

structure.pop()

structure.print_structure()
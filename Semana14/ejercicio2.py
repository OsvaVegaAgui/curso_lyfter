# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    
    data: int
    next: "Node"
    prev: "Node"
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleEndedQueue:
    
    head:Node
    tail:Node
    
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        
        current_node = Node(value)
        
        if self.head is None:
            self.head = current_node
            self.tail = current_node
        else:
            current_node.next = self.head
            self.head.prev = current_node
            self.head = current_node

    def push_right(self, value):
        
        current_node = Node(value)
        
        if self.tail is None:
            self.head = current_node
            self.tail = current_node
        else:
            current_node.prev = self.tail
            self.tail.next = current_node
            self.tail = current_node

    def pop_left(self):
        
        if self.head:
            self.head = self.head.next
            
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        else:
            self.tail = None

    def pop_right(self):
        
        if self.tail:
            self.tail = self.tail.prev
            
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
        else:
            self.head = None

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

structure = DoubleEndedQueue()

structure.push_left(35)
structure.push_right(34)
structure.push_left(33)
structure.push_right(31)

# structure.print_structure()

structure.pop_left()
structure.pop_right()

structure.print_structure()

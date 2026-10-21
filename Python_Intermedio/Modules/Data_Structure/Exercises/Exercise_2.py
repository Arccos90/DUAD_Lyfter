"----------------------------Exercise_2_Structures----------------"
class DequeNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_right (self, data):
        "To add item to the end (right)"
        new = DequeNode(data)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def push_left (self, data):
        "To add item to the beginning (left)"
        new = DequeNode (data)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def pop_left (self):
        "to remove item to the beginning (left)"
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        print(f"Plato retirado en la izquierda: {value}")
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return value

    def pop_right (self):
        "to remove item to the end (right)"
        if self.tail is None:
            return None
        value = self.tail.data
        self.tail = self.tail.prev
        print(f"Plato retirado en la derecha: {value}")
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return value

    def print_structure(self):
        if self.head is None:
            print("La pila esta vacía!!")
            return
        
        print(f"HEAD: {self.head.data}")
        print("---------NODOS---------------")
        actual = self.head
        while actual is not None:
            print(actual.data)
            actual = actual.next

        print("--------------FIN---------------")
        print(f"TAIL: {self.tail.data}")
            

print("""
--------------------------------------------------
        Prueba de Validación                      
--------------------------------------------------
""")
print("-----Deque Vacía------")
d = Deque()
d.print_structure()

print("-----Prueba inserción derecha-------")
d.push_right ("Plato 1")
d.push_right ("Plato 2")
d.print_structure()

print("----Prueba inserción izquierda------")
d.push_left ("Plato 3")
d.push_left ("Plato 4")
d.print_structure()

print("----Prueba inserción combinada------")
d.push_right("Plato 5")
d.push_left ("Plato 6")
d.print_structure()

print("====Prueba remoción derecha e izquierda")
d.pop_left()
d.pop_right()
d.print_structure()

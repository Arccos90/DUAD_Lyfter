class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push (self, data):
        print("Agrega un elemento encima de la pila")
        new_node = Node (data, next=self.head)
        self.head = new_node
        print(new_node.data)

    def pop (self):
        print ("Quitando un plato de la pila")
        if self.head is None:
            print("La pila esta vacía")
            return None
        valor = self.head.data
        self.head = self.head.next
        print(f"{valor}, voy pa'fuera")
        return valor

    def print_stack (self):
        actual = self.head
        print("----- CIMA-------")
        while actual is not None:
            print(f"{actual.data}")
            actual = actual.next





pila = Stack()

first_plate = "soy el primer plato"
pila.push (first_plate)

second_plate = "soy el segundo plato"
pila.push (second_plate)

third_plate = "soy el tercer plato"
pila.push (third_plate)

pila.print_stack()

pila.pop ()
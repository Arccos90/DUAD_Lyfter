class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:

  def __init__(self, head:Node):
    self.head = head

  def print_structure(self):
    current_node = self.head
    print("La estrutura de datos es:")
    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.next

class Queue(LinkedList):
  def enqueue(self, new_node):
    current_node = self.head
    next_node = current_node.next
    while (next_node is not None):
      current_node = next_node
      next_node = current_node.next

    current_node.next = new_node

  def dequeue(self):
    print(f"Nodo eliminado es: {self.head.data}")
    self.head = self.head.next
    


tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
primer_nodo = Node("Soy el primer nodo", segundo_nodo)

queue = Queue(primer_nodo)

print("Agregando un elemento")

queue.enqueue(Node("Soy el nuevo nodo!"))
queue.print_structure()

print("Quitando un elemento")

queue.dequeue()
queue.print_structure()
print("Creating Classes")
class Linkedlistyboi():
	def __init__(self):
		print("Linkedlistyboi Initialised")
		self.start_pointer = None
		self.end_pointer = None
	def traverse(self):
		node1 = self.start_pointer
		traverseLoop = True
		print("Start Traversal")
		while node1.next_pointer != None and traverseLoop:
			print(node1.data)
			print("↓")
			node1 = node1.next_pointer
			if node1.next_pointer == None:
				traverseLoop = False
		print(node1.data)
		print("End Traversal")
		traverseLoop = False
	def add_node(self, NewNode):
		node = self.start_pointer
		previous = None
		loop = True
		print(f"_______Start Adding The Character {NewNode.data}_______")
		while loop and node and start:
			print("The Loops BrOTher")
			if ord(NewNode.data) < ord((self.start_pointer).data):
				node = self.start_pointer
				node.prev_pointer = NewNode
				NewNode.next_pointer = node
				NewNode.prev_pointer = None
				self.start_pointer = NewNode
				print("Proc")
				loop = False
			elif ord(node.data) > ord(NewNode.data):
				#print(node.data)
				NewNode.next_pointer = node
				previous = node.prev_pointer
				node.prev_pointer = NewNode
				node = previous
				NewNode.prev_pointer = node
				#print(node.data)
				node.next_pointer = NewNode
				#print((node.next_pointer).data)
				print("Proc")
				loop = False
			elif ord(NewNode.data) > ord((self.end_pointer).data):
				node = self.end_pointer
				NewNode.next_pointer = None
				NewNode.prev_pointer = node
				node.next_pointer = NewNode
				print("Proc")
				loop = False
			else:
				node = node.next_pointer
				print("next")
		print(f"_______ End  Adding The Character {NewNode.data}_______")
class Node:
	def __init__(self, data):
		self.data = data
		self.next_pointer = True
		self.prev_pointer = True
		print(f"Constructing Node {self.data}")


start = False
a = Linkedlistyboi()
a1 = Node("C")
a2 = Node("D")
a3 = Node("B")
a4 = Node("F")
a5 = Node("X")
a6 = Node("G")
a7 = Node("")
a8 = Node("")

a.start_pointer = a3
a1.next_pointer = a2
a1.prev_pointer = a3
a2.next_pointer = a4
a2.prev_pointer = a1
a3.next_pointer = a1
a3.prev_pointer = None
a4.next_pointer = a6
a4.prev_pointer = a2
a5.next_pointer = None
a5.prev_pointer = a6
a6.next_pointer = a5
a6.prev_pointer = a4
a.end_pointer = a5

start = True

print("/////////////////////////////////////////////")
#print("_______Add the letter A_______")
a.traverse()
a9 = Node("A")
a.add_node(a9)
a.traverse()
print("/////////////////////////////////////////////")
#print("_______Add the Letter E_______")
a.traverse()
a7 = Node("E")
a.add_node(a7)
a.traverse()
#print(a7.prev_pointer.data)  E
#print(a7.next_pointer.data)
#print(a2.prev_pointer.data)  D
#print(a2.next_pointer.data)
#print(a4.prev_pointer.data)  F
#print(a4.next_pointer.data)
print("/////////////////////////////////////////////")
#print("_______Add the letter Z_______")
a.traverse()
a8 = Node("Z")
a.add_node(a8)
a.traverse()
print("/////////////////////////////////////////////")
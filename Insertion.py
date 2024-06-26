class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
     def __init__(self):
        self.head = None

     def insert_begin(self, data):
         data_begin_inserted = Node(data)
         data_begin_inserted.next = self.head
         self.head = data_begin_inserted

     def insert_end(self,data):
         data_end_inserted = Node(data)
         temp = self.head
         while temp.next:
             temp = temp.next
         temp.next = data_end_inserted

     def insert_position(self,data,position):
          data_insert_position = Node(data)  
          temp = self.head 
          for i in range(1,position-1):
              temp = temp.next
          data_insert_position.data = data
          data_insert_position.next = temp.next
          temp.next = data_insert_position


     def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next



sll = SingleLinkedList()

node = Node(10)
sll.head = node 

node2 = Node(20)
sll.head.next = node2

node3 = Node(30)
node2.next = node3

node4 = Node(40)
node3.next = node4

node5 = Node(50)
node4.next = node5

#--- insert-begin------
sll.insert_begin(5)
sll.insert_begin(1)
sll.insert_begin(0)
#----------------------

#------ insert-end-----
sll.insert_end(55)
sll.insert_end(60)
sll.insert_end(65)
#----------------------

#---- insert_position---
sll.insert_position(25,4)
sll.insert_position(26,5)
#-----------------------


sll.display()

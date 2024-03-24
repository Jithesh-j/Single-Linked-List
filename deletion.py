#--------- Deletion of linked list---------------

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    
     def __init__(self):
         self.head = None

     def insert_begin(self,data):
         insert_data_begin = Node(data)
         insert_data_begin.next = self.head
         self.head = insert_data_begin

     def insert_end(self,data):
         insert_data_end = Node(data)  
         temp = self.head
         while temp.next:
             temp = temp.next
         temp.next = insert_data_end

     def insert_position(self, data, pos):
         insert_position = Node(data)
         temp = self.head 
         for i in range(pos -1):
             temp = temp.next
         insert_position.data = data
         insert_position.next = temp.next
         temp.next = insert_position

     def delete_first(self):
         temp =self.head
         self.head = temp.next 
         temp.next = None
     def delete_last(self):
         prev = self.head
         temp = self.head.next
         while temp.next is not None:
             temp = temp.next
             prev = prev.next
         prev.next = None
     def delete_position(self,pos):
         prev = self.head
         temp = self.head.next
         for i in range(pos-1):
             prev = prev.next
             temp = temp.next
         prev.next = temp.next  

     def display(self):
         if self.head is None:
             print("Empty")
         else:
             temp = self.head
             while temp: 
                 print(temp.data, "-->", end= " ")
                 temp = temp.next
     

sll = SingleLinkedList()

node = Node(10)
sll.head = node

node2 = Node(20)
sll.head.next = node2

node3 = Node(30)
node2.next = node3


#-----insert-begin---------
sll.insert_begin(8)
sll.insert_begin(7)
sll.insert_begin(5)
#--------------------------

#------- inser-end---------
sll.insert_end(34)
sll.insert_end(35)
sll.insert_end(36)
sll.insert_end(37)
#--------------------------

#----- insert_position-----
sll.insert_position(23,3)
#--------------------------

#------- delete-first-----
sll.delete_first()
#-------------------------

#---- delete-last------
sll.delete_last()
#----------------------

#-----delete-position------
sll.delete_position(2)
#--------------------------

#------display------
sll.display()
#-------------------

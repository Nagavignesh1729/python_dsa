class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, val):
        curr = self.head

        if curr is None:
            self.head = Node(val)
            self.length = 1
            return
    
        while curr.next:
            curr = curr.next

        new_node = Node(val)
        curr.next = new_node
        self.length += 1

    def length(self):
        return self.length

    def insert_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, val, idx):
        if idx == self.length:
            self.append(val)
            return

        if idx == 0:
            self.insert_front(val)
            return
        
        if idx > self.length or idx < 0:
            print("Index out of bounds.")
            return
        
        new_node = Node(val)
        curr = self.head
        for i in range(1, idx):
            curr = curr.next

        temp = curr.next
        curr.next = new_node
        new_node.next = temp

    #delete by value
    def delete(self, val):
        if self.head is None:
            print("Linked List is empty - no element to delete.")
            return
        
        if self.head.val == val:
            self.head = self.head.next
            return

        curr = self.head
        prev = self.head.next

        while curr and curr.val != val:
            prev = curr
            curr = curr.next

        
        if curr is None:
            print("Value not found in the list.")
            return
        
        prev.next = curr.next
    

    def display(self):
        curr = self.head

        while curr:
            print(f"{curr.val} -> ", end="")
            curr = curr.next

        print("None", end="\n")

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(15)
    ll.append(19)
    ll.display()
    ll.insert(9, 0)
    ll.insert(12, 2)
    ll.display()
    ll.delete(9)
    ll.delete(15)
    ll.delete(19)
    ll.display()


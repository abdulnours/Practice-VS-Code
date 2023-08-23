class Node:
    '''
    An object for storing a single node of a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    '''

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        # returns a string representation of the node
        return "<Node data: %s>" % self.data
    
# python -i linked_list.py
# N1 = Node(10)
# N1
# N2 = Node(20)
# N1.next_node = N2
# N1.next_node

class LinkedList:
    '''
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    '''

    # head = None  <<Created within self.head>>

    def __init__(self):
        self.head = None
    
    def is_empty(self):             # returns a bool = empty status
        '''
        Determines if the linked list is empty
        Takes Constant O(1) time
        '''

        return self.head == None    # or: self.head is None
    
    def size(self):
        '''
        CONVINIENCE METHOD: no added functionality, only makes info more accessible
        Returns the number of nodes in the list 
        Takes Linear O(n) time
        '''

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    # l = LinkedList()
    # N1 = Node(10)
    # l.head = N1
    # l.size()
    
    def add(self, data):
        '''
        Adds a new Node containing data at the head of the list
        Also called 'prepend'
        Constant time O(1)
		'''

        new_head = Node(data)
        new_head.next_node = self.head # type: ignore
        self.head = new_head

    # l = LinkedList()
    # l.add(10)
    # l.size()
    # l.add(20)
    # l.add(30)
    # l.size()

    def __repr__(self):
        '''
        Return a string representation of the list.
        Takes Linear O(n) time.
        '''
        
        nodes = []
        current = self.head

        while current:
            if current is self.head:    # same as current == self.head
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return  '-> '.join(nodes)
    
    # l = LinkedList()
    # l.add(10)
    # l.add(20)
    # l.add(30)
    # l
    
    def search(self, key):
        '''
        Search for the first node containing data that matches the key
        Returns the node or `None` if not found
        Takes O(n) time
        '''

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None
    
    # l = LinkedList()
    # l.add(10)
    # l.add(20)
    # l.add(5)
    # l.add(34)
    # n = l.search(5)
    # n
    # l

    def insert(self, data, index):
        '''
        Inserts a new Node containing data at index position.
        Insertion takes Constant O(1) time but; 
        finding node at insertion point takes Linear O(n) time.
        Takes overall Linear O(n) time.
        '''

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node # type: ignore
                position -= 1

            before = current
            after = current.next_node # type: ignore

            before.next_node = new # type: ignore
            new.next_node = after

    def remove(self, key):
        '''
        Removes Node containing data that matches the key.
        Returns the node or `None` if key doesn't exist.
        Takes Linear O(n) time.
        '''

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node # type: ignore

            else:
                previous = current
                current = current.next_node

        return current
    
    def remove_at_index(self, index):
            
        current = self.head
        position = index

        if index == 0:
            self.head = current.next_node # type: ignore

        elif index > 0:
            
            while position > 1:
                current = current.next_node # type: ignore
                position -= 1

            before = current
            at_index = current.next_node # type: ignore
            after = at_index.next_node # type: ignore
            before.next_node = after # type: ignore
            
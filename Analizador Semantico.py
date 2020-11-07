import hashlib
INITIAL_CAPACITY=10

# Node data structure - essentially a LinkedList node
class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=None

    def __str__(self):
        return (self.key, self.value, self.next != None)

    def __repr__(self):
        return str(self)

# Hash table with separate chaining
class HashTable:
    # Initialize hash table
    def __init__(self):
        self.capacity=INITIAL_CAPACITY
        self.size=0
        self.buckets=[None] * self.capacity

    # Generate a hash for a given key
    # Input:  key - string
    # Output: Index from 0 to self.capacity

    def read_from_file(self):
        file = 'Lectura.txt'
        with open(file) as f_obj:
            for line in f_obj:
                self.insert(self.algorithm_funtion(1,line),line)

    def generator_Hash(self, h):
        digest=h.hexdigest()
        return digest

    def algorithm_funtion(self, algorithm_number, data):
        algorithm=""
        if algorithm_number != 3:
            if algorithm_number == 1:
                '''El sha256 es la longitud de bytes que tendra el hash'''
                algorithm="sha256"
            if algorithm_number == 2:
                '''El sha512 es la longitud de bytes que tendra el hash'''
                algorithm="sha512"
            bdata=bytes(data, 'utf-8')
            h=hashlib.new(algorithm, bdata)
            _hash=self.generator_Hash(h)
            return _hash

    def hash2(self, key):
        multi=1
        hashvalue=0
        for ch in key:
            hashvalue+=multi * ord(ch)
        multi+=1
        # return the remainder of the by dividing hash by the size of the table
        return hashvalue % INITIAL_CAPACITY;

    def hash(self, key):
        hashsum=0
        # For each character in the key
        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashsum+=(idx + len(key)) ** ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]
            hashsum=hashsum % self.capacity
        return hashsum

    # Insert a key,value pair to the hashtable
    # Input:  key - string
    # 		  value - anything
    # Output: void
    def insert(self, key, value):
        # 1. Increment size
        self.size+=1
        # 2. Compute index of key
        index=self.hash2(key)
        # Go to the node corresponding to the hash
        node=self.buckets[index]
        # 3. If bucket is empty:
        if node is None:
            # Create node, add it, return
            self.buckets[index] = Node(key, value)
            return
        # 4. Iterate to the end of the linked list at provided index
        prev=node
        while node is not None:
            prev=node
            node=node.next
        # Add a new node at the end of the list with provided key/value
        prev.next = Node(key, value)

    # Find a data value based on key
    # Input:  key - string
    # Output: value stored under "key" or None if not found
    def find(self, key):
        # 1. Compute hash
        index=self._hash(key)
        # 2. Go to first node in list at bucket
        node=self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node=node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value

    # Remove node stored at key
    # Input:  key - string
    # Output: removed data value or None if not found
    def remove(self, key):
        # 1. Compute hash
        index=self.hash(key)
        node=self.buckets[index]
        prev=None
        # 2. Iterate to the requested node
        while node is not None and node.key != key:
            prev=node
            node=node.next
        # Now, node is either the requested node or none
        if node is None:
            # 3. Key not found
            return None
        else:
            # 4. The key was found.
            self.size-=1
            result=node.value
            # Delete this element in linked list
            if prev is None:
                self.buckets[index]=node.next  # May be None, or the next match
            else:
                prev.next=prev.next.next  # LinkedList delete by skipping over
            # Return the deleted result
            return result
if __name__ == '__main__':
    prueba = HashTable()
    prueba.read_from_file()
    print("Todo bien")
    '''prueba.insert(creaCodidoUnico.algorithm_funtion(1,"Hola"),"Hola")
    prueba.insert(creaCodidoUnico.algorithm_funtion(1,"hola"), "hola")
    prueba.insert(creaCodidoUnico.algorithm_funtion(1,"hola"), "hola")
    prueba.insert(creaCodidoUnico.algorithm_funtion(1,"because yes"), "because yes")
    prueba.insert(creaCodidoUnico.algorithm_funtion(1,"nani"), "nani")'''






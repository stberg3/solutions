class Node():
    __slots__=["neighbors", "key"]
    
    def __init__(self, key):
        self.key=key
        self.neighbors=set()
    
    def __str__(self):
        return "{0}: {1} ".format(self.key, self.neighbors)
    
    def __repr__(self):
        return self.key
    
    def __eq__(self, other):
        return self.key == other.key
    
    def __hash__(self):
        return hash(self.key)
    
class Graph():
    __slots__=["vertices"]
    
    def __init__(self):
        self.vertices=set()
        
    def __str__(self):
        return str([(str(vertex)) for vertex in list(self.vertices)])
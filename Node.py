#tree practice

class Node(object):
    def __init__(self, name, value, child=[], numChild = 0):
        self.name = name;
        self.value = value;
        self.child = []
        self.numChild = 0
        return None

    def getName(self):
        return(self.name)

    def setValue(self, value):
        self.value = value
        return None
    
    def getValue(self):
        return(self.value)

    def getNumChild(self):
        return(self.numChild)

    def showNumChild(self):
        print(self.numChild)
        return None

    def setChild(self, Node):
        self.child.append(Node)
        Node.setParent(self)
        self.numChild += 1;
        return None

    def getChild(self):
        return self.child

    def setParent(self,Node):
        self.parent = Node;
        return None

    def getParent(self):
        return self.Parent

    def showChild(self):
        for child in self.child:
            print(str(child) + '\n \n')
        return None

    def showParent(self):
        print(self.parent)
        return None
    
    def __str__(self):
        return("Node Class\n"+"Object Name: " + str(self.name)+'\n'+"Object Value :"+ str(self.value))


def traverse(start, destination):
    #start, destination are both Node classes
    current = start
    while current.getValue() != destination.getValue():
        print(current)
        if current.getNumChild() > 1:            
            if current.child[0].getValue() > current.child[1].getValue(): #assume binary trees only
                current = current.child[1]
                print(current)
            else:
                current = current.child[0]
                print(current)
        else:
            current = current.getChild()[0]
            print(current)
            
    if current.getChild() == []: #when you reach a leaf node
        current.setValue(None)
        current = current.getParent()
        print(current)

        print(current.getValue())

##### set up
a = Node('a',1)
b = Node('b',3)
c = Node('c',7)
d = Node('d',9)
e = Node('e',12)
f = Node('f',18)
g = Node('g',21)
h = Node('h',37)
i = Node('i',24)
j = Node('j',22)

a.setChild(b)
a.setChild(c)
b.setChild(d)
b.setChild(e)
c.setChild(f)
c.setChild(g)
d.setChild(h)
f.setChild(i)
g.setChild(j)

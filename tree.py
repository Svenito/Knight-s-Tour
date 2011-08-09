class Node:
    def __init__(self, data=None):
        self.parent = None;
        self.children = [];
        self.data = data

    def detach(self):
        self.parent = None;
        for child in children:
            child.parent = None
        children = []

    def getSiblings(self):
        siblings = self.parent.children
        siblings.remove(self)
        return siblings

class Tree:
    def __init__(self):
        self.root = None;

    def isEmtpy(self):
        if self.root is None:
            return True
        return False
       
    def printIt(self, node):
        print node.data
        for c in node.children:
            self.printIt(c)

    def addChild(self, child, parent=None):
        if parent is None:
            self.root = child
            return
        parent.children.append(child)
        child.parent = parent

    def removeChild(self, child):
        child.detach()

    def findChild(self, start_node, data):
        if start_node.data == data:    
            return self.root

        
        for child in start_node.children:
            if child.data == data:
                return node
            self.findChild(child, data)

        return None

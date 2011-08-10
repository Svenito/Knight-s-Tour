class Node:
    def __init__(self, data=None):
        self.parent = None;
        self.children = [];
        self.data = data

    def detach(self):
        self.parent.children.pop(self)
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
       
    def printIt(self, node=None):
        if node is None:
            node = self.root
        print node.data,
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

    def findImmediateChild(self, start_node, data):
        if start_node is None:
            return None
        
        for child in start_node.children:
            if child.data == data:
                return child

        return None

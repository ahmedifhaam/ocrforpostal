class Node:
    pattern = ""
    nodevalue = ""
    parent = ""
    children = {}

    def __init__(self,nodevalue,pattern):
        self.pattern = pattern
        self.nodevalue = nodevalue

    def addChild(self,Node):
        if self.children[Node.pattern] == None :
            self.children[Node.pattern] = []
        self.children[Node.pattern].append(Node)

    def getChildWithPattern(self,pattern):
        if(self.children[pattern]!= None):
            return self.children[pattern]
        else:
            return None

    def getChildWithNode(self,Node):
        return self.getChildWithPattern(Node.pattern)


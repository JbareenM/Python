#!/usr/bin/python
class Node:
    def __init__(self,val):
        self.v=val
        self.l=None
        self.r=None
        self.size=0
class Tree:
    def __init__(self):
        self.root=None
    def Root(self):
        return self.root
    def Add(self,val):
        if self.root==None:
            self.root=Node(val)
        else:
            self.__Add(val,self.root)
    def __Add(self,val,node):
        if val < node.v:
            if node.l != None:
                self.__Add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r != None:
                self.__Add(val, node.r)
            else:
                node.r = Node(val)
    def find(self,val):
        if self.root!=None:
            return self.__find(val,self.root)
        else:
            return None
    def __find(self,val,node):
        if val==node.v:
            return node
        elif val>node.v and node.v!=None:
            return self.__find(val,node.r)
        elif val<node.l and node.l!=None:
            return self.__find(val,node.l)
    def deleteTree(self):
        self.root=None
    def printTree(self):
        if(self.root != None):
            self.__printTree(self.root)
    def __printTree(self,node):
        if(node != None):
            self.__printTree(node.l)
            print(str(node.v) + ' ')
            self.__printTree(node.r)
    def left(self,val):
        n=self.find(val).l
        if n==None:
            return None
        return n.v
    def right(self,val):
        n=self.find(val).r
        if n==None:
            return None
        return n.v

t=Tree()
t.Add(5)
t.Add(6)
t.Add(4)
t.printTree()
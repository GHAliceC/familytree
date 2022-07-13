from typing import List, Dict
from utils import Utils
from member import Node

class TreeOps(Utils):
    def __init__(self):
        Utils.__init__(self)

    def findparent(self,
                   parname: str,
                   **kwargs
                   ) -> Node:

        self.root = self.grabTree()
        currNode = None

        if self.root is None:
            return currNode

        stack = []
        stack.append(self.root)
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode.name == parname:
                return currNode
            for ch in currNode.child:
                stack.append(ch)
        return None

    def addchild(self,
                 parent: Node,
                 childname: str,
                 childspouse: str,
                 grandchild: List,
                 **kwargs
                 ) -> bool:
        if parent is None:
            return False
        # print("childname:", childname, "childspouse:", childspouse, "grandchild:", grandchild, "bros:", parent.child)
        member = Node(childname)
        member.spouse = childspouse

        for grdchild in grandchild:
            member.child.append(Node(grdchild))

        for ch in parent.child:
            if ch.name == childname:
                return True

        parent.child.append(member)
        self.storeTree(self.root)
        return True

    def editnode(self,
                 parent: Node,
                 childname: str,
                 newname: str,
                 childspouse: str="",
                 bdate: str="",
                 ddate: str="",
                 **kwargs
                 ) -> bool:
        if parent is None:
            return False

        print("parent: ", parent.name, parent.spouse)
        print("member: ", childname, newname, childspouse, bdate, ddate)
        for ch in parent.child:
            if ch.name == childname:
                ch.name = newname
                if bdate != "" and bdate != ch.bdate:
                    ch.bdate = bdate
                if ddate != "" and ddate != ch.ddate:
                    ch.ddate = ddate
                if childspouse != "" and childspouse != ch.spouse:
                    ch.spouse = childspouse

        self.storeTree(self.root)

        return True

    def delnode(self,
                parent: Node,
                childname: str,
                **kwargs
                ) -> bool:
        if parent is None:
            return False

        print(parent.child, childname)
        numOfchild = len(parent.child)
        noOfchild = -1
        for idx in range(numOfchild):
            if parent.child[idx].name == childname:
                noOfchild = idx
                break

        if idx != -1:
            parent.child.pop(idx)
            self.storeTree(self.root)
            return True

        return False

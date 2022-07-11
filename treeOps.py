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

        while stack:
            currNode = stack.pop()
            print("running member:", currNode.name)
            if currNode.name == parname:
                return currNode

            if currNode.child != []:
                for ch in currNode.child:
                    stack.append(ch)

        return currNode

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
        print("child:", member.name, member.spouse)

        for grdchild in grandchild:
            member.child.append(Node(grdchild))

        print("parent.child:", parent.name, parent.child)
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

        for ch in parent.child:
            if ch.name == childname:
                ch.name = newname
                if not bdate:
                    ch.bdate = bdate
                if not ddate:
                    ch.ddate = ddate
                if not childspouse:
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

        numOfchild = len(parent.child)
        noOfchild = -1
        for idx in range(numOfchild):
            if parent.child[idx].name == childname:
                noOfchild = idx
                break

        if idx != -1:
            parent.child.pop(idx)
            return True

        self.storeTree(self.root)

        return False

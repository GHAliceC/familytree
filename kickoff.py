class Node:
    def __init__(self, name):
        self.name = name
        self.spouse = "?"
        self.bdate = "?"
        self.ddate = "?"
        self.child = []

def storeTree(root: Node,
             export: str="tree.p")->None:
    import pickle
    fw = open(export, "wb")
    pickle.dump(root, fw)
    fw.close()

def grabTree(filename: str="tree.p")->Node:
    import pickle
    fr = open(filename, "rb")
    return pickle.load(fr)
        
def buildtree()->Node:
    root = Node("TinggangLin")
    subroot = Node("SongzhaoLin")
    subroot.spouse = "LiyingSu"
    daughter = Node("JianhuaLin")
    daughter.spouse = "JianqiangChen"
    daughter.child.append(Node("YuweiChen"))
    son = Node("DongmingLin")
    son.spouse = "XiaojuChen"
    son.child.append(Node("XuwenLin"))
    subroot.child.append(daughter)
    subroot.child.append(son)
    root.child.append(subroot)
    root.child.append(Node("SuijuanLin"))
    root.child.append(Node("SongguangLin"))
    
    return root

root = buildtree()
storeTree(root)

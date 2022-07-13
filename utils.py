import os
import time
import joblib
import collections
from member import Node
from typing import List, Dict

cwd = os.getcwd()


class Utils:
    def __init__(self):
        self.memo_path = "tree.p"

    def levelOrderTraversal(self,
                            root: Node
                            ) -> List:
        ans = []

        # Return Null if the tree is empty
        if root is None:
            return ans

        # Initialize queue
        queue = collections.deque()
        queue.append(root)

        # Iterate over the queue until it's empty
        while len(queue) > 0:
            # Check the length of queue
            currSize = len(queue)
            currList = []

            while currSize > 0:
                # Dequeue element
                currNode = queue.popleft()
                # currList.append(currNode.name)
                currList.append(currNode)
                currSize -= 1

                # Check for child list
                for ch in currNode.child:
                    queue.append(ch)

            # Append the currList to answer after each iteration
            ans.append(currList)

        # Return answer list
        return ans

    def write2txt(self,
                  lst: List,
                  filename: str = "static/linfamily.txt"
                  ) -> bool:
        print(lst)
        try:
            with open(os.path.join(cwd, filename), "w") as f:
                line = ""
                for n in range(len(lst)):
                    print("n: ", n)
                    for person in lst[n]:
                        line += person.name
                        if not person.spouse:
                            person.spouse = "?"
                        line += " + " + person.spouse + "\n"
                        if person.child != []:
                            line += " c: "
                            for ch in person.child:
                                line += ch.name + ", "
                            line = line[:-2] + "\n"
                        line += f" n: This is generation {n} in Lin's family\n"
                        line += person.name + "\n"
                        line += " l: " + person.bdate + " - " + person.ddate + "\n"
                        line += " n: put other info. here\n"
                print("line: \n", line)
                f.write(line)
            return True
        except Exception as e:
            print(str(e))
            return False

    def storeTree(self,
                  root: Node) -> None:
        joblib.dump(root, os.path.join(cwd, self.memo_path))
        print("here1")
        self.write2txt(self.levelOrderTraversal(root))
        print("here2")

    def grabTree(self) -> Node:
        fr = joblib.load(os.path.join(cwd, self.memo_path))
        return fr

    

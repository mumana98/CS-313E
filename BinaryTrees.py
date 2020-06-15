import os

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    def __init__ (self):
        self.root = None

  # insert data into the tree
    def insert (self, data):
        new_node = Node (data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node
                
    # Returns true if two binary trees are similar
    def is_similar (self, fNode, pNode):
        if fNode == None and pNode == None:
            return True
        elif fNode.data == pNode.data and self.is_similar(fNode.lchild, pNode.lchild) and self.is_similar(fNode.rchild, pNode.rchild):
            return True
        return False

    # Prints out all nodes at the given level
    def print_level (self, aNode, level):
        if aNode == None:
            return
        elif level == 1:
            print(aNode.data, end=" ")

        self.print_level(aNode.lchild, level - 1)
        self.print_level(aNode.rchild, level - 1)

    # Returns the height of the tree
    def get_height (self, aNode): 
        if aNode == self.root:
            return max(0 + self.get_height(aNode.lchild), 0 + self.get_height(aNode.rchild))
        elif aNode != None:
            #print("add")
            return max(1 + self.get_height(aNode.lchild), 1 + self.get_height(aNode.rchild))
        else:
            return 0

    # Returns the number of nodes in tree which is 
    # equivalent to 1 + number of nodes in the left 
    # subtree + number of nodes in the right subtree
    def num_nodes (self, aNode):
        if aNode != None:
            return 1 + self.num_nodes(aNode.lchild) + self.num_nodes(aNode.rchild)
        else:
            return 0


    def printTree(self, aNode):
        if aNode != None:
            self.printTree(aNode.lchild)
            print(aNode.data)
            self.printTree(aNode.rchild)


def main():
    nodes = input().strip().split()
    tree1 = Tree()
    nodes2 = input().strip().split()
    tree2 = Tree()

    for i in nodes:
        tree1.insert(i)
    for j in nodes2:
        tree2.insert(j)
    print("The Trees are similar:", tree1.is_similar(tree1.root, tree2.root))
    print("")
    #print(tree1.num_nodes(tree1.root))
    #tree1.printTree(tree1.root)
    #print(tree1.get_height(tree1.root))
    print("Levels of Tree 1:", end="")
    for i in range(tree1.get_height(tree1.root)+2):
        tree1.print_level(tree1.root, i)
        print("")
    print("")
    print("Levels of Tree 2:", end="")
    for i in range(tree2.get_height(tree2.root)+2):
        tree2.print_level(tree2.root, i)
        print("")
    print("")
    
    print("Height of Tree 1:", tree1.get_height(tree1.root))
    print("Nodes in Tree 1:", tree1.num_nodes(tree1.root))


    print("Height of Tree 2:", tree2.get_height(tree2.root))
    print("Nodes in Tree 2:", tree2.num_nodes(tree2.root))


main()
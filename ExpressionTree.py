import os

# list of operators (tree parents)
operators = ['+','-','*','/','//','%','**']

class Stack (object):
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        return (len(self.stack) == 0)
    def size(self):
        return (len(self.stack))

class Node (object):
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None
        #self.parent = None
        #self.visited = False

class Tree (object):
    def __init__ (self):
        self.root = Node(None)
        
    def create_tree (self, expr):
        s = Stack()
        expr = expr.split()
        #print(expr)

        current = self.root
        #current = Node(current)

        for i in expr:
            if i.isdigit():
                current.data = i
                current = s.pop()
            
            elif i == '(':
                s.push(current)
                current.l_child = Node(None)
                current = current.l_child

            elif i in operators:
                current.data = i
                s.push(current)
                current.r_child = Node(None)
                current = current.r_child

            elif i == ')':
                if s.size() > 0:
                    current = s.pop()
            
            else:
                print(i)
                current.data = i
                if not s.is_empty():
                    current = s.pop()

              
    def evaluate (self, aNode):
        #['+','-','*','/','//','%','**']
        #print(type(aNode.data))
        if aNode.data == '+':
            return (self.evaluate(aNode.l_child) + self.evaluate(aNode.r_child))
        elif aNode.data == '-':
            return (self.evaluate(aNode.l_child) - self.evaluate(aNode.r_child))
        elif aNode.data == '*':
            return (self.evaluate(aNode.l_child) * self.evaluate(aNode.r_child))
        elif aNode.data == '/':
            return (self.evaluate(aNode.l_child) / self.evaluate(aNode.r_child))
        elif aNode.data == '//':
            return (self.evaluate(aNode.l_child) // self.evaluate(aNode.r_child))
        elif aNode.data == '%':
            return (self.evaluate(aNode.l_child) % self.evaluate(aNode.r_child))
        elif aNode.data == '**':
            return (self.evaluate(aNode.l_child) ** self.evaluate(aNode.r_child))
        elif aNode.data.isdigit():
            #print(aNode.data)
            return (int(aNode.data))
        else:
            return (float(aNode.data))

    def pre_order (self, aNode, strg):
        if (aNode != None):
            #print (aNode.data, end=" ")
            strg += str(aNode.data) + " "
            strg = self.pre_order (aNode.l_child, strg)
            strg = self.pre_order (aNode.r_child, strg)
        return strg


    def post_order (self, aNode, strg):
        if (aNode != None):
            strg = self.post_order (aNode.l_child, strg)
            strg = self.post_order (aNode.r_child, strg)
            strg += str(aNode.data) + " "
            #print (aNode.data, end=" ")
            #print("aNode.data:",aNode.data)
        #print(strg)
        return strg 


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    expr = input().strip()
    tree1 = Tree()
    tree1.create_tree(expr)
    fptr.write(str(expr))
    fptr.write(" = ")
    fptr.write(str(float(tree1.evaluate(tree1.root))))
    fptr.write("\n")
    fptr.write("\nPrefix Expression: ")
    fptr.write(tree1.pre_order(tree1.root, ""))
    fptr.write("\n")
    fptr.write("\nPostfix Expression: ")
    fptr.write(tree1.post_order(tree1.root, ""))
    

main()
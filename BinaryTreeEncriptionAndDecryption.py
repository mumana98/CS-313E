import os

class Node(object):
    def __init__ (self, data = None):
        self.data = data
        self.rchild = None
        self.lchild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        self.en_str = encrypt_str

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        chn = 0
        if ch.isalpha():
            ch = ch.lower() #convert to lowercase
        chn = ord(ch) #convert to ascii value

        new_n = Node(chn) #makes a node out of ch
        
        if self.root == None: #if tree is empty, become the root
            self.root = new_n 
        else:
            if self.search_dupes(new_n.data) == None: #search for duplicates, duplicates are not added
                curr = self.root
                parent = self.root
                while curr != None:
                    parent = curr
                    if chn < curr.data:
                        curr = curr.lchild
                    else:
                        curr = curr.rchild
                
                if chn < parent.data:
                    parent.lchild = new_n
                else:
                    parent.rchild = new_n

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        cstr = "*"
        curr = self.root
        if curr.data != ch:
            cstr = ""

        while (curr != None) and (curr.data != ch):
            if ch < curr.data:
                curr = curr.lchild
                cstr += "<"
            else:
                curr = curr.rchild
                cstr += ">"
        return cstr + "!"

    # looks for duplicates given a character value
    def search_dupes (self, ch):
        curr = self.root
        while (curr != None) and (curr.data != ch):
            if ch < curr.data:
                curr = curr.lchild
            else:
                curr = curr.rchild
        return curr

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        curr = self.root
        #print(self.search(ord(" ")))
        for i in st:
            if i == "<":
                curr = curr.lchild
            elif i == ">":
                curr = curr.rchild
        return curr.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        new_st = []

        for i in st:
            if i.isalpha():
                i = i.lower() #convert to lowercase
                #self.insert(i)
            new_st.append(i)

        encryption = ""

        for k in new_st:
            #print(k)
            if k.isalpha():
                encryption += self.search(ord(k))
            elif k == " ":
                encryption += self.search(ord(k))

        return encryption[:-1]


    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        new_str = ""
        st = st.split("!")
        for i in st:
            #print(i)#cypher version of char
            #print((self.traverse(i)))
            if self.traverse(i) == 32:
                new_str += " " 
            else:
                new_str += chr(self.traverse(i))

        return new_str

    def printTree(self, aNode):
        if aNode != None:
            self.printTree(aNode.lchild)
            print(chr(aNode.data))
            self.printTree(aNode.rchild)
    
def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    key = input().strip()
    #print(key)
    #print(ord(" "))
    encrypt_string = input().strip()
    decrypt_string = input().strip()
    #print(encrypt_string, decrypt_string)
    tree1 = Tree(key)
    for i in key:
        tree1.insert(i)
    #tree1.printTree(tree1.root)
    fptr.write(tree1.encrypt(encrypt_string))
    fptr.write("\n")
    fptr.write(tree1.decrypt(decrypt_string))
    #tree1.traverse(tree1.root)
    
    
main()
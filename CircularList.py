import os

class Link(object):
    def __init__(self,d):
       self.data=d


class CircularList(object):
    # Constructor
    def __init__ ( self ): 
        self.numlinks=0
        self.first=None

    # Insert an element (value) in the list
    def insert ( self, data ):
        
        if self.numlinks == 0:
               self.first = Link(data)

        elif self.numlinks == 1:
            curr = self.first
            
            curr.next = Link(data)
            curr.next.next = self.first
            curr.prev = self.first.next
            curr.prev.prev = self.first
            

        else: 
            first = self.first
            curr = self.first
            while curr.next != first:
                curr = curr.next
            curr.next = Link(data)
            curr.next.prev = curr
            curr.next.next = self.first
            curr.next.next.prev = curr.next
        self.numlinks += 1


    # Find the link with the given data (value)
    def find ( self, data ):

        if(self.first.data == data):
            return self.first

        curr = self.first.next
        first = self.first
        while curr != first:
            if curr.data == data:
                return curr
            curr = curr.next
        return None



    # Delete a link with a given data (value)
    def delete ( self, data ):
        del_it = Link(data)
        curr = self.first
        first = self.first
        while curr != first:
            if curr == del_it:
                curr.prev.next = curr.next
                self.numlinks -=1
            curr = curr.next
        return None


    # Delete the nth link starting from the Link start 
    # Return the next link from the deleted Link
    def delete_after ( self, start, n):
        i = 1
        curr = self.find(start)
        while i < (n):
            curr = curr.next
            i+= 1
        if curr == self.first:
            self.first = curr.next
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        self.numlinks -=1
        return curr.prev.next, curr
    # Return a string representation of a Circular List
    def __str__ ( self ):
        string = ""
        curr = self.first
        for i in range(self.numlinks):
            if curr and curr.data != None:
                string= string + '' + str(curr.data)
                curr = curr.next
        return string
        
def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    soldiers = int(input().strip())
    start = int(input().strip())
    count = int(input().strip())
    
    final_sol = CircularList()
    for i in range(1, soldiers+1):
        final_sol.insert(i)
        next_start = start
    for i in range(soldiers - 1):
        new_start, shot = final_sol.delete_after(next_start, count)
        shot = shot.data
        next_start = new_start.data
        
        fptr.write(str(shot))
        fptr.write("\n")
    fptr.write(str(final_sol))

    


main()

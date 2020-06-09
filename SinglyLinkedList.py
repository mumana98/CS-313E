class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    # initialize the linked list
    def __init__ (self, first):
        self.first = None

    # get number of links 
    def get_num_links (self):
        current = self.first
        total = 0
        while(current != None):
            total+=1
            current = current.next
        return total

    # add an item at the beginning of the list
    def insert_first (self, data): 
        newLink = Link (data)
        newLink.next = self.first
        self.first = newLink
    # add an item at the end of a list
    def insert_last (self, data): 
        newLink = Link (data)
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink
    # add an item in an ordered list in ascending order
    def insert_in_order (self, data): 
        newLink = Link (data)
        current = self.first

        if (current == None):
            newLink.next = self.first
            self.first = newLink
            return

        if newLink.data < self.first.data:
            newLink.next = self.first
            self.first = newLink
            return

        while(current.next is not None and
            current.next.data < newLink.data): 
            current = current.next
              
        newLink.next = current.next
        current.next = newLink 
    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        current = self.first
        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current
    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        current = self.first
        if (current == None):
            return None

        while (current.data != data):
            if (current.next > data):
                return None
            else:
                current = current.next

        return current
    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current
    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        current = self.first
        while(current != None):
            print(current, end="  ")
            current = current.next

    # Copy the contents of a list and return new list
    def copy_list (self):
        new_lst = LinkedList()
        current = self.first
        while(current != None):
            new_lst.insert_last(current.data)
            current = current.next

        return new_lst
        
    # Reverse the contents of a list and return new list
    def reverse_list (self): 
        new_lst = LinkedList()
        current = self.first
        while(current != None):
            new_lst.insert_first(current.data)
            current = current.next

        return new_lst
          

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self):  
        newList = LinkedList()
        current = self.first
        if(self.first == None):
            return None
        while(current != None):
            newList.insert_in_order(current.data)
            current = current.next
        return(newList)

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        current = self.first
        previous = self.first
        if current == None:
            return False
        while current >= previous:
            if current == None:
                return True
            current = current.next
            previous = current
        return False
    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        current = self.first
        return current == None
            
    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other): 
        current1 = self.first
        current2 = other.first

        temp = None
    
        # List1 is empty then return List2 
        if current1 is None: 
            return current2 
    
        # if List2 is empty then return List1 
        if current2 is None: 
            return current1 
    
        # If List1's data is smaller or 
        # equal to List2's data 
        if current1.data <= current2.data: 
    
            # assign temp to List1's data 
            temp = current1 
    
            # Again check List1's data is smaller or equal List2's  
            # data and call mergeLists function. 
            temp.next = merge_list(current1.next, current2) 
            
        else: 
            # If List2's data is greater than or equal List1's  
            # data assign temp to current2 
            temp = current2 
    
            # Again check List2's data is greater or equal List's 
            # data and call mergeLists function. 
            temp.next = merge_list(current1, current2.next) 
    
        # return the temp list. 
        return temp 

        
        # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        current = self.first
        current2 = other.first
        while(current != None and current2 != None):
            if current.data != current2.data:
                return False
            current = current.next
            current2 = current2.next
        return True
        
    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        new_lst = LinkedList()
        current = self.first
        if current == None:
            return
        while current != None:
            print(new_lst.find_unordered(current))
            print(current)
            print()
            if new_lst.is_empty():
                new_lst.insert_first(current)
            elif new_lst.find_unordered(current) != current:
                new_lst.insert_last(current)
            else:
                new_lst.insert_last(current)
            current = current.next
        return new_lst

def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    pass
    # Test method insert_last()

    # Test method insert_in_order()

    # Test method get_num_links()

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 

    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 

    # Test method delete_link()
    # Consider two cases - data is there, data is not there 

    # Test method copy_list()

    # Test method reverse_list()

    # Test method sort_list()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()

    # Test method merge_list()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    # Test remove_duplicates()

if __name__ == "__main__":
    main()
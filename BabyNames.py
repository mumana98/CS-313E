#  File: BabyNames.py 

#  Description: Be able to read info from a file and properly input the info into a dictionary. Be able to extract certain data from the dictionary

#  Student Name:  Matthew Umana

#  Student UT EID:  msu245

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 

#  Date Last Modified:


class BabyNames(object):
	
    # Initializes the dictionary that will hold all the baby names
    def __init__(self):
	    # key: name
	    # value: list of ranks
	    self.names = {}


    # Reads in the file and adds to the dictionary
    def fill_data(self, file_name):
        try:
            f = open(file_name, encoding = 'utf8')

            while True:
                line = f.readline()
                
                if not line: 
                    break
                else:
                    line = line.split()
                    self.names[line[0]] = line[1:len(line)]
            return self.names
        
        except FileNotFoundError as excpt:
            print("File name, " + file_name + " not found")

	
    # True if a name exists in the dictionary and False otherwise.
    def contains_name(self, name):
        if str(name) in self.names:
            return True
        else:
            return False
                

    # Returns all the rankings for a given name. Assume the name exists
    def find_ranking(self, name):
        decade = 1900
        if self.contains_name(name):
            print(name, end=" ")
            for dec in self.names[name]:
                print(dec, end=" ")
            print("\n")
            for i in self.names[name]:
                print(str(decade) + ": " + i)
                decade += 10    
        else:
            print(str(name) + " does not exist.")

    
	# Returns a list of names that have a rank in all the decades in sorted order by name.
    def ranks_of_all_decades(self):
        name_dict = self.names
        num_names = 0
        lst_names = []
        counter = 0
        in_each_dec = True
        for i in name_dict:
            for j in name_dict[i]:
                if int(j) > 0:
                    in_each_dec = True
                else:
                    in_each_dec = False
                    break
                counter += 1
            
            if in_each_dec:
                num_names += 1
                lst_names.append(i)
            else:
                continue

        print(str(num_names) + " appear in every decade. The names are:")
        for i in lst_names:
            print(i)


	# Returns a list of all the names that have a rank in a given decade in order of rank.
    def ranks_of_a_decade(self, decade):
        d = 1900
        counter = 0
        dct = dict()
        for i in self.names:
            d = 1900
            counter = 0
            name = self.names[i]
            for j in name:
                if (name[counter] != '0') and (d == decade):
                    dct[i] = j
                d += 10
                counter += 1

        print("\nThe names are in order of rank:")
        for key, value in sorted(dct.items(), key=lambda item: item[1]):
            print("%s: %s" % (key, value))


	# Return all names that are getting more popular in every decade. The list must be sorted by name.
    def less_popular(self):
        asc_lst = []
        num = 0
        for i in self.names:
            name = self.names[i]
            name = list(map(int, name))
            name2 = name.copy()
            if name2[-1] == 0:
                name2[-1] = 1001
            name2.sort()
            
            if (name == name2) and name2[0] != 0:
                asc_lst.append(i)
                num += 1
        print(num, "names are less popular in every decade.")
        for j in asc_lst:
            print(j)
        print()


	# Return all names that are getting less popular in every decade. The list must be sorted by name.
    def getting_popular(self):
        asc_lst = []
        num = 0
        
        for i in self.names:
            name = self.names[i]
            name = list(map(int, name))
            name2 = name.copy()
            name2.sort(reverse=True)
            if (name == name2) and 0 not in name[:-1]:
                asc_lst.append(i)
                num += 1
        print(num, "names are more popular in every decade.")
        for j in asc_lst:
            print(j)
        print()


def main():
    b = BabyNames()
    b.fill_data("names.txt")
    user_input = ''
    options = ["\nOptions:",
                   "Enter 1 to search for names",
                   "Enter 2 to display data for one name.",
                   "Enter 3 to display all names that appear in one decade in order of rank.",
                   "Enter 4 to display all names that appear in all decades.",
                   "Enter 5 to display all names that are more popular in every decade.",
                   "Enter 6 to display all names that are less popular in every decade.",
                   "Enter 7 to quit"]
    while user_input != '7':
        for i in range(len(options)):
            print(options[i])
        user_input = input("Enter choice: ")
        if user_input == '1':
            name = input("Enter a name: ").capitalize()
            print()
            if b.contains_name(name):
                print("The matches with their highest ranking decade are:")
                dec = 1900
                int_lst = []
                for i in b.names[name]:
                    int_lst.append(int(i))
                for j in int_lst:
                    if j == min(int_lst):
                        print(name, dec, "\n")
                        break
                    dec += 10
            else:
                print(name, "does not appear in any decade.\n")
                
        elif user_input == '2':
            name = input("Enter a name: ").capitalize()
            print()
            if b.contains_name(name):
                b.find_ranking(name)

        elif user_input == '3':
            dec = int(input("Enter decade: "))
            if dec <= 2000 and dec >= 1900:
                b.ranks_of_a_decade(dec)
            else:
                print("No data on this decade.")

        elif user_input == '4':
            b.ranks_of_all_decades()

        elif user_input == '5':
            b.getting_popular()
            print()
            
        elif user_input == '6':
            b.less_popular()
            print()
            
        elif user_input == '7':
            print("\nGoodbye.")


if __name__ == "__main__":
    main()

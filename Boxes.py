#  File: Boxes.py

#  Description: given the dimensions (length width and height) of 20 boxes, 
#  find the largest combination of boxes that can fit inside of each other

#  Student Name: Matthew Umana 

#  Student UT EID: msu245

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 03/07/20

#  Date Last Modified: 03/09/20

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes(box_list, sub_set, idx, all_box_subsets):
    hi = len(box_list)
    if idx == hi:
        all_box_subsets.append(sub_set)
        return all_box_subsets
    else:
        c = sub_set[:]
        sub_set.append(box_list[idx])
        sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
        sub_sets_boxes(box_list, c, idx + 1, all_box_subsets)
        

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes):
    largest_size = 0
    nesting_list = []
    for subset in all_box_subsets:
        count = 0
        is_long = False
        for box in range(0, len(subset)-1):
            if does_fit(subset[box], subset[box+1]) == False:
                is_long = False
                break
            else:
                count += 1
                is_long = True
        
        if largest_size < count:
            largest_size = count

        if is_long:
            nesting_list.append(subset) 
    
    for sub in nesting_list:
        if len(sub) > largest_size:
            all_nesting_boxes.append(sub)
            
    return all_nesting_boxes

# returns True if box1 fits inside box2
def does_fit (box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # open the file for reading
    in_file = open ("boxes.txt", "r")

    # read the number of boxes
    line = in_file.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int (box[j])
        box.sort()
        box_list.append (box)

    # close the file
    in_file.close()

    # sort the box list
    box_list.sort()

    # create an empty list to hold all subset of boxes
    all_box_subsets = []

    # create a list to hold a single subset of boxes
    sub_set = []

    # generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)

    # initialize the size of the largest sub-set of nesting boxes
    largest_size = 0

    # create a list to hold the largest subsets of nesting boxes
    all_nesting_boxes = []

    # go through all the subset of boxes and only store the
    # largest subsets that nest in all_nesting_boxes
    largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes)

    # print all the largest subset of boxes
    print("Largest Subset of Nesting Boxes")
    for sub in all_nesting_boxes:     
        for i in range(len(sub)):
            print(sub[i])
        print()

if __name__ == "__main__":
  main()

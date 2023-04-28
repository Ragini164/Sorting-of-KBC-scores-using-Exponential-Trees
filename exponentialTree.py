import csv

class Node:
    def __init__(self):
        self.data = []       # stores the data (name and score) at that node
        self.children = []   # stores references to the child nodes of that node.

class ExponentialTree:
    def __init__(self, b=3):
        self.b = b            # branching factor
        self.root = Node()    # create root node

    def insert(self, name, score):
        node = self.root       # start at root node
        while node.children:   # while there are still child nodes to explore
            index = self.binary_search(node.data, score)  # find the index where the new data should be inserted
            node = node.children[index]    # move to the appropriate child node
        node.data.append((name, score))    # add the new data to the current node
        node.data.sort(key=lambda x: x[1], reverse=True)  # sort the data in descending order by score

        if len(node.data) == self.b:    # if the node is full
            self.split(node)            # split the node

    def split(self, node):
        left = Node()       # create new left node
        right = Node()      # create new right node
        mid = self.b // 2   # find the middle index
        left.data = node.data[:mid]   # set left node data
        right.data = node.data[mid+1:]    # set right node data
        node.data = [node.data[mid]]       # set current node data to be the middle element
        node.children = [left, right]     # set current node children to be the left and right nodes

    def binary_search(self, arr, score):
        lo, hi = 0, len(arr)-1      # set lower and upper bounds
        while lo <= hi:             # while there is still a range of indices to search
            mid = (lo + hi) // 2    # find the middle index
            if arr[mid][1] == score:     # if the middle score is equal to the target score
                return mid               # return the middle index
            elif arr[mid][1] > score:     # if the middle score is greater than the target score
                lo = mid + 1              # search the upper half of the range
            else:                         # if the middle score is less than the target score
                hi = mid - 1              # search the lower half of the range
        return lo    # return the index where the target score should be inserted
    
    
    def write_sorted(self):
        values = []        # list to store all data in the tree
        stack = [(self.root, 0)]   # create stack to hold nodes to visit, starting with the root node
        while stack:       # while there are still nodes to visit
            node, index = stack.pop()   # get the next node to visit and its index
            if node.children:           # if the node has children
                stack.extend((child, i) for i, child in enumerate(node.children[::-1]))  # add the children to the stack in reverse order
            values.extend(node.data)    # add the node's data to the list of all data

        sorted_values = sorted(values, key=lambda x: x[1], reverse=True)   # sort the data in descending order by score
        return sorted_values

    def print_sorted(self):
        values = [] # list to store all data in the tree
        stack = [(self.root, 0)] # initialize the stack with the root node and its index
        while stack:
            node, index = stack.pop() # get the node and index at the top of the stack
            if node.children: # if the node has children, add them to the stack in reverse order
                stack.extend((child, i) for i, child in enumerate(node.children[::-1]))
            values.extend(node.data) # add the data in the node to the values list

        sorted_values = sorted(values, key=lambda x: x[1], reverse=True) # sort the values list by score in descending order
        for name, score in sorted_values: # iterate through the sorted values list and print the names and scores
            print(f"{name}: {score}")



# read data from scores.csv file
with open("scores.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

# create an exponential tree and insert each name and score
# for i in range (2,10):
    # start = time.time()
branching_factor = 3
tree = ExponentialTree(b=branching_factor)
for name, score in data:
    tree.insert(name, int(score))
# end = time.time()
# print the sorted data in descending order
tree.print_sorted()

# # print the sorted data in descending order
# tree.print_sorted()

# # write the sorted data to a new file called sorted_scores.csv
# tree.write_sorted("sorted_scores.csv")



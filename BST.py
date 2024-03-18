import sys
import numpy as np
 
# Implement a priority queue data structure using max-heap.
# Do not modify the given function signatures. You are free to add helper functions or variables inside class.

class PriorityQueue:
  def __init__(self, maximum_size):
    self.data = [0] * maximum_size
    self.maximum_size = maximum_size
    self.actual_size = 0

  # Question 1.1 (20 points): Build the priority queue given a list of elements
  def BuildQueue(self, input):
    N = len(input)
    for i in range(N):
      self.data[i] = input[i]

    #print("The elements in priority Queue are: ", end = "")
    self.data = sorted(self.data, reverse = True)
    #print(self.data)
 



  # Add a key into the priority queue
  def Enqueue(self, x):
    self.data.append(x)
    self.data = sorted(self.data, reverse = True)
  


  # Remove a highest priority (largest) key from the priority queue
  def Dequeue(self):
    pop1 = self.data[0]
    self.data[0] = 0
    self.data = sorted(self.data, reverse = True)
    return pop1



# Implement a binary search tree data structure
# Do not modify the given function signatures. You are free to add helper functions or variables inside class.


class TreeNode:
  def __init__(self):
    self.key = 0
    # These are of type 'TreeNode
    self.parent = None
    self.leftchild = None
    self.rightchild = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  # Add an key into the BST. You can assume that there will be no duplicated keys
  def Insert(self, x):
    self.root = self.Insert_Recursive_Call(self.root, x)

  def Insert_Recursive_Call(self, root, x):
    if root is None:
        root = TreeNode()
        root.key = x
        return root

    if x < root.key:
        root.leftchild = self.Insert_Recursive_Call(root.leftchild, x)
    elif x > root.key:
        root.rightchild = self.Insert_Recursive_Call(root.rightchild, x)

    return root

  # Search for a key in the BST. Return true/false to indicate if the key exist or not
  def Search(self, x):
    return self.Search_Recursive_Call(self.root, x)

  def Search_Recursive_Call(self, root, x):
    if root == None:
        return False

    if x == root.key:
        return True
    elif x < root.key:
        return self.Search_Recursive_Call(root.leftchild, x)
    else:
      return self.Search_Recursive_Call(root.rightchild, x)

  # Delete a key in the BST. The key may or may not exist in the BST before deletion.
  def Delete(self, x):
    self.root = self.Delete_Recursive_Call(self.root, x)

  def Delete_Recursive_Call(self, root, x):
    if root is None:
      return root

    if x < root.key:
        root.leftchild = self.Delete_Recursive_Call(root.leftchild, x)
    elif x > root.key:
        root.rightchild = self.Delete_Recursive_Call(root.rightchild, x)

    else:
          # Node with only one child
          if root.leftchild is None:
              return root.rightchild
          elif root.rightchild is None:
              return root.leftchild
          
          # Node with two children
          root.key = self.Find_Min_Value(root.rightchild)
          root.rightchild = self.Delete_Recursive_Call(root.rightchild, root.key)

    return root

  def Find_Min_Value(self, root):
    min_value = root.key
    while root.leftchild is not None:
      min_value = root.leftchild.key
      root = root.leftchild
    return min_value
  
  def Find_Max_Value(self, root):
    max_value = root.key
    while root.rightchild is not None:
      max_value = root.rightchild.key
      root = root.rightchild
    return max_value

  # Find and return  the minimum key in the BST.
  def Minimum(self):
    if self.root is None:
      return None

    current_min = self.root
    while current_min.leftchild is not None:
      current_min = current_min.leftchild

    return current_min.key

  # Question 2.5 (10 points): Find and return the maximum key in the BST.
  def Maximum(self):
    if self.root is None:
      return None

    current_max = self.root
    while current_max.rightchild is not None:
      current_max = current_max.rightchild

    return current_max.key

  # Find and return the successor of a key in the BST. If the successor does not exist, return -1.
  def Successor(self, x):
    current = self.root
    successor = None

    while current is not None:
      if x < current.key:
          successor = current
          current = current.leftchild
      elif x > current.key:
          current = current.rightchild
      else:
          if current.rightchild is not None:
              successor = self.Find_Min_Value(current.rightchild)
          break

    return -1 if successor is None else successor


  # Find and return  the predcessor of a key in the BST. If the predcessor does not exist, return -1.
  def Predcessor(self, x):
    current = self.root
    predcessor = None

    while current is not None:
      if x > current.key:
          predcessor = current
          current = current.rightchild
      elif x < current.key:
          current = current.rightchild
      else:
          if current.leftchild is not None:
              predcessor = self.Find_Max_Value(current.leftchild)
          break

    return -1 if predcessor is None else predcessor


#************ Do not modify code below this line ***************

def verify_array(a, b, size):
  #print(a)
  if (len(a) < size or len(b) < size):
    return False
  for i in range(0, size):
    if (a[i] != b[i]):
     #print(a[i],b[i])
     return False
  return True

def subtree_max_value(root):
  if (root == None):
    return -sys.maxsize - 1
  children_max = max(subtree_max_value(root.leftchild), subtree_max_value(root.rightchild))
  return max(root.key, children_max)

def subtree_min_value(root):
  if (root == None):
    return sys.maxsize
  children_min = min(subtree_min_value(root.leftchild), subtree_min_value(root.rightchild))
  return min(root.key, children_min)

def verify_tree(root):
  if (root == None):
    return True
  if (root.leftchild != None and root.key <= subtree_max_value(root.leftchild)):
    return False
  if (root.rightchild != None and root.key >= subtree_min_value(root.rightchild)):
    return False
  return verify_tree(root.leftchild) and verify_tree(root.rightchild)

result = [16, 15, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Name: {} blazer_id: {}".format(name, blazer_id))

print("---------- Priority Queue ---------\n")
pq = PriorityQueue(15)
pq.BuildQueue([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
pass_check = verify_array(pq.data, [16, 14, 10, 9, 8, 7, 4, 3, 2, 1], 10)
print(f"BuildQueue: {'Pass' if pass_check else 'No Pass'}")
pq.Enqueue(12)
pass_check = verify_array(pq.data, [16, 14, 12, 10, 9, 8, 7, 4, 3, 2, 1], 11)
print(f"Enqueue(12): {'Pass' if pass_check else 'No Pass'}")
pq.Enqueue(5)
pass_check = verify_array(pq.data, [16, 14, 12, 10, 9, 8, 7, 5, 4, 3, 2, 1], 12)
print(f"Enqueue(5): {'Pass' if pass_check else 'No Pass'}")
pq.Enqueue(15)
pass_check = verify_array(pq.data, [16, 15, 14, 12, 10, 9, 8, 7, 5, 4, 3, 2, 1], 13)
print(f"Enqueue(15): {'Pass' if pass_check else 'No Pass'}")
pq.Enqueue(6)
pass_check = verify_array(pq.data, [16, 15, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 14)
print(f"Enqueue(6): {'Pass' if pass_check else 'No Pass'}")
pq.Enqueue(11)
pass_check = verify_array(pq.data, [16, 15, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 15)
print(f"Enqueue(11): {'Pass' if pass_check else 'No Pass'}")
for i in range(0, 15):
  x = pq.Dequeue()
  pass_check = x == result[i]
  print(f"Dequeue current_node max  {'Pass' if pass_check else 'No Pass'}")

print("---------- Binary Search Tree ---------\n")
bst = BinarySearchTree()
input = [5, 3, 8, 1, 4, 6, 9, 2, 0, 7, 10, 11, 12]
for i in range(0, len(input)):
  bst.Insert(input[i])
  pass_check = verify_tree(bst.root)
  print("Insert key {}: {}".format(input[i], 'Pass' if pass_check else 'No Pass'))

for i in range(0, len(input)):
  pass_check = bst.Search(input[i])
  print("Search key {}: {}".format(input[i], 'Pass' if pass_check else 'No Pass'))

for i in range(13, 20):
  pass_check = not bst.Search(i)
  print("Search key {}: {}".format(i, 'Pass' if pass_check else 'No Pass'))

pass_check = bst.Minimum() == 0
print(f"Minimum key: {'Pass' if pass_check else 'No Pass'}")
pass_check = bst.Maximum() == 12
print(f"Maximum key: {'Pass' if pass_check else 'No Pass'}")

#print(input)
for i in range(0, len(input)-1):
  pass_check = bst.Successor(input[i]) == input[i]+1
  #print(i, bst.Successor(input[i]), input[i]+1)
  print("Successor of key {}: {}".format(input[i], 'Pass' if pass_check else 'No Pass'))

for i in range(1, len(input)):
  pass_check = bst.Predcessor(input[i]) == input[i]-1
  print("Predcessor of key {}: {}".format(input[i], 'Pass' if pass_check else 'No Pass'))

for i in range(0, len(input)):
  bst.Delete(input[i])
  pass_check = not bst.Search(input[i])
  print("Delete key {}: {}".format(input[i], 'Pass' if pass_check else 'No Pass'))

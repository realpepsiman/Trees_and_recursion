import random
import matplotlib as plt
import time

class TreeNode:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def build_tree(keys):
    root = None
    for key in keys:
        root = insert(root, key)
    return root




def tree_search(root, x):
    if root.key == x:
        # base case: root's key is the target value
        return True
    elif root.left == None and root.right == None:
        # base case: root has no child nodes. Target is not in tree
        return False
    elif x < root.key:
        # recursive case: target value is less than root's key, search left child
        return tree_search(root.left, x)
    else:
        # recursive case: target value is greater than root's key, search right child
        return tree_search(root.right, x)
    

times = []
n = 1000
x = 9990
keys = list(range(1, n+1))
for _ in range(1000):

    random.shuffle(keys) # shuffle key order so trees are random
    
    root = build_tree(keys)
    
    begin = time.time()
        
    found_it = tree_search(root, x)

    elapsed = time.time() - begin
    times.append(elapsed)

plt.hist(times) ;
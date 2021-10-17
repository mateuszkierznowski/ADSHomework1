class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def build_tree(preOrder_seq, InOrder_seq):
    if len(InOrder_seq) > 1:
        tNode = Node(preOrder_seq[0])
        #join InOrder list to create string
        inOrder_j = "".join(InOrder_seq)

        #split obtained string into 2 list by prdeorder sequence
        tNode.left, tNode.right = inOrder_j.split(preOrder_seq[0])

        #romove used value
        preOrder_seq.remove(preOrder_seq[0])

        #converse obtained strings from line 13 into nodes
        tNode.left = build_tree(preOrder_seq, list(tNode.left))
        tNode.right = build_tree(preOrder_seq, list(tNode.right))
        return tNode
    else:
        #when there is no value to split on create node from single value
        if len(preOrder_seq) > 0:
            tNode = Node(preOrder_seq[0])
            preOrder_seq.remove(preOrder_seq[0])
        else:
            #When value doesnt appear converse it to None (otherwise it's string equel to  "")
            return None
        return tNode



def printInorder(node):
    if node is None:
        return

    # first recur on left child
    printInorder(node.left)

    # then print the data of node
    print("\t", node.data)

    # now recur on right child
    printInorder(node.right)

def printpostorder(node):
    if node is None:
        return

    # first recur on left child
    printpostorder(node.left)
    # second recur on right child
    printpostorder(node.right)

    # then print the data of node
    print("\t", node.data)

def printpreorder(node):
    if node is None:
        return

    # print the data of node
    print("\t", node.data)

    # recur on left child

    printpreorder(node.left)

    # then print the data of node
    printpreorder(node.right)



def print2DUtil(root, space):
    COUNT = [10]
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    for i in range(COUNT[0], space):
        print(end=" ")

    print(root.data)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)
import func
import const as c


if __name__ == "__main__":
    node = func.build_tree(c.preOrder, c.inOrder)

    print("Display tree: \n")
    func.print2D(node)

    print("Inorder traversal: \n")
    func.printInorder(node)

    print("Postorder traversal: \n")
    func.printpostorder(node)

    print("Preorder traversal: \n")
    func.printpreorder(node)



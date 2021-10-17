# ADSHomework1
Construct Tree from given Inorder and Preorder traversals

Using dependency that spliting list by first not used preorder sign such as:

preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

inOrder = ['D', 'B', 'E', 'A', 'F', 'C']

preOrder first sign = A

split inOrder list by A:

            A
       DBE     FC
       
 Code uses that dependecy by recurension such as every time first element of preOrder list is removed.
 T

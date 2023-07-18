Tree:[str] = ["A",["B",["D",[],[]],[]],["C",["E",["G",[],[]],[]], ["F",[],[]]]]
def treeRoot(aTree):
    if aTree:
        return aTree[0]

def treeLeft(aTree):
    if aTree:
        return aTree[1]

def treeRight(aTree):
    if aTree:
        return aTree[2]

print(f"Root: {treeRoot(Tree)}")
print(f"Left-subtree: {treeLeft(Tree)}")
print(f"Right-subtree: {treeRight(Tree)}")
print("Inorder-Traversal of tree gives us: ")
def inorderTraversal(tree):
    if tree:
        inorderTraversal(tree[1])
        print(tree[0],end=", ")
        inorderTraversal(tree[2])

inorderTraversal(Tree)
print()
def inorderTraversal_FromBook(tree):
    if tree:
        inorderTraversal_FromBook(treeLeft(tree))
        print(treeRoot(tree),end=", ")
        inorderTraversal_FromBook(treeRight(tree))

inorderTraversal_FromBook(Tree)
print()
def preOrderTraversal(tree):
    if tree:
        print(treeRoot(tree),end=", ")
        preOrderTraversal(treeLeft(tree))
        preOrderTraversal(treeRight(tree))
print("The Pre-order traversal of tree gives us: ",end="[")
preOrderTraversal(Tree)
print("]")

def postOrderTraversal(tree):
    if tree:
        postOrderTraversal(treeLeft(tree))
        postOrderTraversal(treeRight(tree))
        print(treeRoot(tree),end=", ")

print("The postorder traversal of tree gives us: ",end="[")
postOrderTraversal(Tree)
print("]")
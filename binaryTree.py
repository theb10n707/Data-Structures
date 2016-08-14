from __future__ import print_function

#Node class
class Node:

    #initialize node with an item
    def __init__(self, item):
        self.left   = None
        self.right  = None
        self.top    = None
        self.item   = item

#Binary Tree
class BinaryTree:
    #initialize tree with a root node
    def __init__(self, item):
        self.root = Node(item)

    #get root of tree
    def getRoot(self):
        return self.root

    #add node to tree helper
    def addNode(self, item):
        #begin function at the root
        self.add(item, self.root)

    #add node logic
    def add(self, item, node):
        #add node to left side
        if item < node.item:
            #add node to left bottom
            if node.left == None:
                node.left = Node(item)
                node.left.top = node
            #continue recursively until no more left nodes are found
            else:
                self.add(item, node.left)
        #add node to right side
        else:
            #add node to right bottom
            if node.right == None:
                node.right = Node(item)
                node.right.top = node
            #continue recursively until no more right nodes are found
            else:
                self.add(item, node.right)

    #find node helper
    def findNode(self, item):
        #begin function at root
        return self.find(item, self.root)

    #find node logic
    def find(self, item, node):
        #items match, return node
        if item == node.item:
            return node
        #item is on the left side
        elif item < node.item and node.left != None:
            return self.find(item, node.left)
        #item is on the right side
        elif item > node.item and node.right != None:
            return self.find(item, node.right)

    #print tree helper
    def printTree(self, order):
        #choose order and begin at root
        if order == "pre":
            self.printPreOrder(self.root)
        elif order == "in":
            self.printInOrder(self.root)
        elif order == "post":
            self.printPostOrder(self.root)

    #print tree logic preorder
    def printPreOrder(self, node):
        if node != None:
            print(str(node.item), end=" ")
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    #print tree logic inorder
    def printInOrder(self, node):
        if node != None:
            self.printInOrder(node.left)
            print(str(node.item), end=" ")
            self.printInOrder(node.right)

    #print tree logic postorder
    def printPostOrder(self, node):
        if node != None:
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(str(node.item), end=" ")

    #delete node helper
    def deleteNode(self, item):
        #begin function at root
        return self.delete(item, self.root)

    #delete node logic
    def delete(self, item, node):
        #find if node exist in tree
        delNode = self.find(item, node)
        if delNode == None:
            return "Node is not in the Tree"
        #delete a node with no children
        elif delNode.left == None and delNode.right == None:
            if delNode.item < delNode.top.item:
                delNode.top.left = None
            else:
                delNode.top.right = None
        #delete node with 1 left child
        elif delNode.left != None and delNode.right == None:
            if delNode.item > delNode.top.item:
                delNode.top.right = delNode.left
            else:
                delNode.top.left = delNode.left
        #delete node with 1 right child
        elif delNode.left == None and delNode.right != None:
            if delNode.item < delNode.top.item:
                delNode.top.left = delNode.right
            else:
                delNode.top.right = delNode.right
        #delete node with 1 left and 1 right child
        elif delNode.left != None and delNode.right != Node:
            oldNode = delNode.left
            #find a replacement value for the node
            while oldNode.right != None:
                oldNode = oldNode.right
            delNode.item = oldNode.item
            if oldNode.left != None:
                oldNode.top.right = oldNode.left
            else:
                oldNode.top.right = None



tree = BinaryTree(5)
tree.addNode(10)
tree.addNode(3)
tree.printTree("pre")
tree.deleteNode(3)
tree.printTree("pre")
tree.addNode(17)
tree.addNode(12)
tree.addNode(9)
tree.printTree("in")

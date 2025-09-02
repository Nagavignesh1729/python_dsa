class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_function_(self.root, val)

    def insert_list(self, l):
        for val in l:
            self.insert(val)

    def _insert_function_(self, node, val) -> TreeNode:
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_function_(node.left, val)
        elif val > node.val:
            node.right = self._insert_function_(node.right, val)

        return node

    def inorder(self) -> list:
        if not self.root:
            return []
        return self._inorder_function_(self.root)

    def _inorder_function_(self, node):
        if not node:
            return []
        return self._inorder_function_(node.left) + [node.val] + self._inorder_function_(node.right)
    
    def delete(self, val) -> None:
        if not self.root:
            print("No tree found. Delete operation failed.")
            return
        self._delete_function_(self.root, val)

    
    def _delete_function_(self, node, key):
        if not node:
            return None
    
        if key < node.val:
            node.left = self._delete_function_(node.left, key)
        elif key > node.val:
            node.right = self._delete_function_(node.right, key)
        # the node that has to be deleted is found
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            # the deleting node has both children 
            # ==> then we find the leftmost node of its right subtree (next inorder element)
            else:
                # find the successor that replaces our current node (next inorder)
                next = self._next_inorder_helper_(node.right)
                node.val = next.val
                # recursively delete the successor node
                node.right = self._delete_function_(node.right, node.val)
        return node

    def _next_inorder_helper_(self, node) -> TreeNode:
        while node.left:
            node = node.left
        return node
        

if __name__ == "__main__":
    # testing the functionalities

    tree = Tree()
    tree.insert_list([10, 20, 5, 1, 6, 15, 30, 13, 14, 15])
    print(tree.inorder())
    tree.delete(15)
    print(tree.inorder()) # expect a sorted array

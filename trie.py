class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.child:
                current.child[c] = TrieNode()
            current = current.child[c]

        current.end = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.child:
                return False
            current = current.child[c]

        return current.end
    
    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.child:
                return False
            current = current.child[c]

        return True
    
    def delete(self, word: str) -> None:
        if not self.root.child:
            return
        self._delete_function_(self.root, word)

    def _delete_function_(self, node: TrieNode, word: str) -> bool:
        # base case - when we reach the end of the word
        if not word:
            # child node exists --> so don't delete the node (just set the marker false)
            if len(node.child) > 0:
                node.end = False
                # false indicated this node can't be deleted
                return False
            # no children --> this node can be deleted
            else:
                return True

        # recursive case - word has characters left
        else:
            if word[0] in node.child:
                can_delete_child = self._delete_function_(node.child[word[0]], word[1:])
                if can_delete_child:
                    del node.child[word[0]]

                    # we decide if this itself can be deleted or not
                    # can delete if no children and not end of another word
                    return len(node.child) == 0 and (not node.end)
                else:
                    return False
            # character not found case --> no deletion
            else:
                return False
            
    def allWords(self) -> list:
        l = []
        if not self.root.child:
            return []
        self._all_words_(self.root, l, "")
        return l

    def _all_words_(self, node, res, curr_word) -> None:
        # base case - when we see a marker (end of a word)
        if node.end == True:
            res.append(curr_word)
        
        # recursive case --> call on all the children
        for k in node.child:
            self._all_words_(node.child[k], res, curr_word+k)

if __name__ == "__main__":
    # testing code
    test_trie = Trie()
    words = ["app", "apple", "man", "mango", "still", "start", "star"]

    for word in words:
        test_trie.insert(word)

    print("Search apple: ", test_trie.search("apple"))
    print("Search appl: ", test_trie.search("appl"))
    print("StartsWith sti: ", test_trie.startsWith("sti"))
    test_trie.delete("apple")
    print("apple deleted")
    print("Search apple: ", test_trie.search("apple"))
    print("Search app: ",test_trie.search("app"))
    print("StartsWith appl: ", test_trie.startsWith("appl"))
    print(test_trie.allWords())

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endofWord = False
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        d = self.root.children
        #print(d)
        for c in word:
            if c not in d:
                node = TrieNode()
                d[c] = node
            else:
                node = d[c]
            d = node.children
            n1 = node
        n1.endofWord = True


    def search(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.endofWord


    def startsWith(self, prefix):
        d = self.root.children
        for i in prefix:
            if i not in d:
                return False
            else:
                d = d[i].children
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
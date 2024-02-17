class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def to_index(self,char):
        return ord(char)-ord('a')

    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            index= self.to_index(char)
            if node.children[index] is None:
                node.children[index]=TrieNode()
            node=node.children[index]
        node.end=True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = self.to_index(char)
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = self.to_index(char)
            if not node.children[index]:
                return False
            node = node.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
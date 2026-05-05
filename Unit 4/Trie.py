# Trie Node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


# Trie
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # Search exact word
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    # Prefix search
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# Main
t = Trie()

n = int(input("Enter number of words: "))
print("Enter words:")

for _ in range(n):
    word = input().strip()
    t.insert(word)

# Search
word = input("Enter word to search: ")
print("Search:", t.search(word))

# Prefix
prefix = input("Enter prefix to check: ")
print("StartsWith:", t.startsWith(prefix)) 
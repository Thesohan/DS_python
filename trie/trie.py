class Node:
    def __init__(self):
        self.leaf = False
        self.children = {}
        self.word = ''
        self.parent = None


class Trie:
    def __init__(self):
        self.root = Node()

    def get_node(self):
        return Node()

    def insert(self, item):
        temp_root = self.root
        for char in item:
            if not temp_root.children.get(char):
                temp_root.children[char] = self.get_node()
                temp_root.children[char].parent = temp_root
                temp_root.word += char
            temp_root = temp_root.children[char]
        temp_root.leaf = True
        print(f"{item} inserted")

    def search(self, item):
        current = self.root
        for char in item:
            if current.children.get(char):
                current = current.children[char]
            else:
                print(f"{item} not found")
                return False, None
        if current.leaf:
            print(f"{item} found")
            return True, current
        print(f"{item} not found")
        return False, None

    def delete(self, item):
        is_present, current_root = self.search(item)
        if is_present:
            current_root.leaf = False
            if not current_root.children:
                temp = current_root.parent
                del current_root
                current_root = temp
                while current_root and not current_root.leaf:
                    temp = current_root.parent
                    del current_root
                    current_root = temp
            print(f"{item} deleted")

if __name__ == '__main__':
    input = ["sohan", "mohan", "rohan", "mohni", "mintu", "neet", "iit"]
    trie = Trie()
    for item in input:
        trie.insert(item)
    for item in input:
        trie.delete(item)
    trie.delete("mummy")
    trie.search("sohan")

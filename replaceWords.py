class Node:
    def __init__(self):
        self.children = {}
        self.end = False

    def __repr__(self):
        return f'{self.children}'


class Trie:
    def __init__(self):
        self.root = Node()


def replaceWords(dictionary, sentence):
    root = Trie()
    t = root.root

    for word in dictionary:
        for w in word:
            if w not in t.children:
                t.children[w] = Node()
            t = t.children[w]
        t.end = True
        t = root.root

    root_node = root.root
    indexes = []
    split = sentence.split()

    for idx, word in enumerate(split):
        string = ''
        for w in word:
            print(w, string)
            if w in root_node.children:
                string += w
                root_node = root_node.children[w]
                print(root_node.end, root_node.children)
            else:
                break
            if root_node.end:
                indexes.append((idx, string))
                break

        root_node = root.root

    for i in indexes:
        split[i[0]] = i[1]

    return " ".join(split)


print(replaceWords(["bat", "rat", "cat"],
                   "the cattle was rattled by the battle"))

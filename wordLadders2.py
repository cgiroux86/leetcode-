class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        stack = [[beginWord]]
        results = []
        combos = set()
        shortest_path = float('inf')

        while stack:
            path = stack.pop()
            curr = path[-1]
            if curr == endWord:
                if len(path) < shortest_path:
                    i = 0
                    shortest_path = len(path)
                    while i < len(results):
                        if len(results[i]) > shortest_path:
                            results.pop(i)
                            i += 1
                    results.append(path)
                    combos.add("".join(path))
                elif len(path) == shortest_path and "".join(path) not in combos:
                    results.append(path)
                continue
            # if curr not in combos:
            #     combos.add(curr)
            for i in range(len(curr)):
                for letter in alpha:
                    list_copy = list(curr)
                    list_copy[i] = letter
                    path_copy = path.copy()
                    string = "".join(list_copy)
                    if string in wordList and string not in path_copy:
                        path_copy.append("".join(list_copy))
                        stack.append(path_copy)
        return results if results[0] else []


s = Solution()

print(s.findLadders("ta",
                    "if",
                    ["ts", "sc", "ph", "ca", "jr", "hf", "to", "if", "ha", "is", "io", "cf", "ta"]))

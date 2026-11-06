class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            curr = node
            for i in range(idx, len(word)):
                char = word[i]
                if char == '.':
                    for key in curr:
                        if key != '#' and dfs(i+1, curr[key]):
                            return True
                    return False
                else:
                    if char not in curr:
                        return False
                    curr = curr[char]
            return '#' in curr
        return dfs(0, self.root)

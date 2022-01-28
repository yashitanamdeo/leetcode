# Problem Statement: https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary(object):

    def __init__(self):
        self.dict, self.len2word  = defaultdict(set), defaultdict(set)

    def addWord(self, word):
        # self.dict: key is combination of index and character, value is a word set whose i-th letter is c
        for i, c in enumerate(word): self.dict[(i, c)].add(word)
        # self.len2word: key is length of word, value is a word set whose length is equal to key
        self.len2word[len(word)].add(word)

    def search(self, word):
        ans = copy.deepcopy(self.len2word[len(word)])
        for i, c in enumerate(word):
            if c != '.': ans &= self.dict[(i, c)]
        return True if len(ans) else False
        
# Alternate Solution
'''
class WordDictionary:

    def __init__(self):
        self.d = collections.defaultdict(list)
        

    def addWord(self, word: str) -> None:
        self.d[len(word)] += [word]
        

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.d[len(word)]
        for x in self.d[len(word)]:
            for i in range(len(word)):
                if word[i] != x[i] and word[i] != '.':
                    break
            else:
                return True
        return False
'''

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
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
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
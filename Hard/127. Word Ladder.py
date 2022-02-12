# Problem Statement: https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:    
        visited = set([beginWord])
        wordSet = set(wordList)
        startSet, endSet = set([beginWord]), set([endWord])
        if endWord not in wordSet:
            return 0        
        return self.bfs(startSet, endSet, visited, wordSet)
        
    def bfs(self, startSet, endSet, visited, wordSet):            
        steps = 1
        while startSet and endSet:
            if len(startSet) > len(endSet):
                startSet, endSet = endSet, startSet
            steps += 1
            nextSet = set()
            for word in startSet:      
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + ch + word[i+1:]
                        if newWord in endSet:
                            return steps
                        if newWord in wordSet and newWord not in visited:
                            nextSet.add(newWord)
                            wordSet.remove(newWord)
                            visited.add(newWord)
            startSet = nextSet
            
        return 0
# Problem Statement: https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        word = ""
        for i in range(len(title)):
            if len(title[i]) < 3:
                word = word + title[i].lower() + " "
            else:
                word = word + title[i].capitalize() + " "
        return word[:-1]

# Alternate Solution
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        word = []
        for i in range(len(title)):
            if len(title[i]) < 3:
                word.append(title[i].lower())
            else:
                word.append(title[i].capitalize())
        return " ".join(word)

# Post: https://leetcode.com/problems/capitalize-the-title/discuss/1716077/python-easy-solution
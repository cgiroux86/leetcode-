from math import floor


class Solution:
    def reorderSpaces(self, text):
        spaces = 0
        words = []
        flag = False
        start, end = 0, 0
        for i in range(len(text)):
            if text[i] == ' ':
                spaces += 1
                if flag:
                    end = i
                    words.append(text[start:end])
                    flag = False
                start, end = 0, 0
            if text[i] != ' ':
                if not flag:
                    start = i
                flag = True
        if spaces == 0:
            return text
        if flag:
            words.append(text[start:])
        if len(words) == 1:
            return "".join(words[0] + " " * spaces)
        s = floor(spaces / (len(words) - 1))
        r = spaces % (len(words) - 1)
        res = "".join((x + " " * s for x in words[0:-1]))
        res += words[-1] + ' ' * r
        return res

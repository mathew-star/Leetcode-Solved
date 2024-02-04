class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        n = len(words)
        
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if int(words[j][-1]) < int(words[min_index][-1]):
                    min_index = j

            # Swap the words
            words[i], words[min_index] = words[min_index], words[i]

        return ' '.join([word[:-1] for word in words])


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        if set(alpha) - set(sentence):
            return False
        else:
            return True
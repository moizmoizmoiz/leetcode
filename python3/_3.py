# O(n)
# was told ln 15 is inefficient since .index method of O(n)
# TODO: use enumerate function

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        max_sequence = ""
        current_sequence = ""
        for ch in s:
            if ch in current_sequence:
                if len(current_sequence) > len(max_sequence):
                    max_sequence = current_sequence
                    # resetting the current sequence by deleting the first repitition of the
                    # current 'ch' in the current sequence and anything before that chr
                    # and continue with the new ch 
                current_sequence = current_sequence[currÍent_sequence.index(ch) + 1:] + ch
            else:
                current_sequence += ch
        return max(len(max_sequence), len(current_sequence))  
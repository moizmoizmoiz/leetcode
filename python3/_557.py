# O(n)
# using split and join function in python3
# TODO: use 2 pointer approach for practice


class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split(" ")
        split_list = [i[::-1] for i in split_list]
        return " ".join(split_list)
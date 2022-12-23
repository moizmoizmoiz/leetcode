# using deque : https://docs.python.org/3/library/collections.html#module-collections
# O(n-log-n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # init list as deque O(n) space
        number_deque = collections.deque(nums)
        reverse_sorted_squares = []

        while number_deque:
            # squaring both ends of the deque before appending and popping
            left_square = number_deque[0] ** 2
            right_square = number_deque[-1] ** 2

            if left_square > right_square:
                reverse_sorted_squares.append(left_square)
                number_deque.popleft()
            else:
                reverse_sorted_squares.append(right_square)
                number_deque.pop()

            # return sorted ascending
        return reverse_sorted_squares[::-1]
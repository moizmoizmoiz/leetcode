# O(n)
# i did not realise one solution means there is only one possible combination
# i misunderstood it as only one combination using the largest number possible
# paired with the difference will be accepted as the correct answer

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            s = numbers[left] + numbers[right]

            #  if number is too big then the larger end is decreased
            if s > target:
                right -= 1
            # else the smaller end is increased
            else:
                left += 1

        return [left + 1, right + 1]
# O(n)
#The idea is to:
#step1: reverse the list
#step2: reverse elements in range as -> 0..k
#step3: reverse back the remaining elements to original order -> k..L

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %=len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        #step1    step2 ^      step3 ^

#------------------------The following solution has a better runtime-------------
# TODO: study why this works better even thought approach is similar
# https://leetcode.com/problems/rotate-array/solutions/1729973/python3-in-place-exaplained/?envType=study-plan&id=algorithm-i&orderBy=most_votes&languageTags=python3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
	    L = len(nums)
	    if L == k: return

	    k = k%L # the case when k > L
	    nums.reverse()

	    for i in range(k//2):
		    nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

	    for i in range(k, (L+k)//2):
		    nums[i], nums[L-1-i+k] = nums[L-1-i+k], nums[i]
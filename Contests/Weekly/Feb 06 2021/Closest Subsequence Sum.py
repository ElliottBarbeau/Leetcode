# Looks like DP but I honestly have no clue how to solve it - haven't done enough DP yet to
# solve this one it seems

'''
You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. 
That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.
'''
class Solution:
    def minAbsDifference(self, nums, goal):
        print()
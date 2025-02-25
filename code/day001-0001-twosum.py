"""
1. 两数之和 (Two Sum)

题目描述：
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，
并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

示例：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]

解题思路：
使用哈希表存储遍历过的数字及其下标。对于每个数字，检查 target - 当前数字 是否在哈希表中，
如果存在，则找到答案；如果不存在，将当前数字及其下标加入哈希表。

时间复杂度：O(n)
空间复杂度：O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i  in  range(len(nums)):
            temp = target - nums[i]
            if temp in map:
                return [map[temp],i]
            map[nums[i]] = i
        return [-1,-1]
    
    
    # 测试代码
def test_two_sum():
    solution = Solution()
    
    # 测试用例1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert solution.twoSum(nums1, target1) == [0, 1]
    
    # 测试用例2
    nums2 = [3, 2, 4]
    target2 = 6
    assert solution.twoSum(nums2, target2) == [1, 2]
    
    # 测试用例3
    nums3 = [3, 3]
    target3 = 6
    assert solution.twoSum(nums3, target3) == [0, 1]
    
    # 测试用例4：无解的情况
    nums4 = [1, 2, 3, 4]
    target4 = 10
    assert solution.twoSum(nums4, target4) == [-1, -1]
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_two_sum()

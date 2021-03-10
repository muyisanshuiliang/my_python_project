#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   496. 下一个更大元素 I.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/3 16:58   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
 
提示：
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
nums1和nums2中所有整数 互不相同
nums1 中的所有整数同样出现在 nums2 中
 
进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？
'''

# import lib
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if not nums1:
        #     return None
        # result = [-1] * len(nums1)
        # if not nums2:
        #     return result
        # for item_inx, item_val in enumerate(nums1):
        #     if not nums2.__contains__(item_val):
        #         continue
        #     index = nums2.index(item_val) + 1
        #     while index < len(nums2):
        #         if nums2[index] > item_val:
        #             result[item_inx] = nums2[index]
        #             break
        #         index += 1
        # return result

        # 根据 nums2 将中间的元素依次放入dict中，其中 key 是当前值，value是 后面比它大的第一个值
        hash_dict = dict()
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                hash_dict[stack.pop()] = i
            stack.append(i)
        return [hash_dict.get(i, -1) for i in nums1]


solution = Solution()
print(solution.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 2, 6, 7, 4]))
print(solution.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))

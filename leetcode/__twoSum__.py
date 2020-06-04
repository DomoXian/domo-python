"""
两数之和
地址：https://leetcode-cn.com/problems/two-sum/
实现思路 左右指针
"""
# !/usr/bin/python


class TwoSum:
    def twosum(self, nums, target):
        hashMap = {}
        for index, num in enumerate(nums):
            flag = hashMap.get(target-num)
            if flag is not None:
                return [index, flag]
            else:
                hashMap[num] = index

t = TwoSum()
list = {1, 2, 3, 34, 5, 5}
result = t.twosum(list, 37)
print(result)

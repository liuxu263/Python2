#!
# -*- coding: utf-8 -*-

''

__author__ = "lx"

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


def twoSum(nums, target):
    l = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(i)
                print(j)
                l.append(i)
                l.append(j)
    return l


if __name__ == "__main__":
    l = [2, 7, 11, 15]
    target = 9
    result = twoSum(l, target)
    print(result)

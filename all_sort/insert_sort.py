# coding:utf-8
"""
------------------------------- 插入排序 --------------------------------------
一、介绍
    插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
二、步骤
    通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
"""


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, n):
        # j = [1, 2, 3, n-1]
        # i 代表内层循环起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break


def insert_sort1(L):
    # 假设第一个是排好序的，从第二个开始正向遍历到最后
    for i in range(1, len(L)):
        temp = L[i]  # 将当前位置的值赋给一个变量
        # 如果i>0 和 i前面数的值大于i对应的值，则交换L[i]和L[i-1]位置
        while i > 0 and L[i - 1] > temp:
            L[i] = L[i - 1]
            # 改变当前i的指针，因为要拿未排序的第一个值和前面所有的值对比
            i = i - 1
            L[i] = temp
    return L


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)

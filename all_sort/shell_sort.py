# coding:utf-8
"""
------------------------------- 希尔排序 --------------------------------------
一、介绍
    希尔排序（Shell Sort）也是插入排序的一种。也称为缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
    希尔排序是非稳定排序算法。该方法因DL.Shell于1959年提出而得名。
二、步骤
    将待排序列划分为若干组，在每一组内进行插入排序，以使整个序列基本有序，然后再对整个序列进行插入排。
"""

def shell_sort(alist):
    """希尔排序"""
    # n=9
    n = len(alist)
    # gap =4
    gap = n // 2
    # i = gap
    # for i in range(gap, n):
    #     # i = [gap, gap+1, gap+2, gap+3... n-1]
    #     while:
    #     if alist[i] < alist[i-gap]:
    #         alist[i], alist[i-gap] = alist[i-gap], alist[i]

    # gap变化到0之前，插入算法执行的次数
    while gap > 0:
        # 插入算法，与普通的插入算法的区别就是gap步长
        # 默认是有第一个元素了。
        for j in range(gap, n):
            # j = [gap, gap+1, gap+2, gap+3, ..., n-1]
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)
# L = [4,2,6,7,9,2,3,5,44,21,41,23,99]
# 数据生成
import random


def getrandata(num):
    L = []
    i = 0
    while i < num:
        L.append(random.randint(0, 100))
        i += 1
    return L


# 插入排序
def insert_sort(L):
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


# 冒泡排序
def bub_sort(L):
    for i in range(len(L) - 1):
        # 每次会排出一个最大的值，最大的值会放在最后面，
        # 所以每一次遍历都比最开始少遍历i次，所以用len(L)-i-1/len(L)-i
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


# 冒泡排序优化版（循环次数最少）
def bubble_sort(L):
    # i=0
    l = len(L)
    while l > 0:
        isSorted = 1
        for i in range(l - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                isSorted = 0  # 加标记，如果又发生交换则记录为0
        if isSorted == 1:  # 如果这一趟没有发生交换说明已经完成排序
            break
        l = l - 1
    return L


# 选择排序
def sel_sort(L):
    for i in range(len(L) - 1):
        # 从i+1个开始，一直到最后一个，拿来与第i个进行比较
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L


# 快速排序
'''
方法一：该方法的基本思想是：
1．先从数列中指定一个数作为基准数。
2．进行分区，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。
'''


def qk_sort(L, left, right):
    if left >= right:
        return L
    key = L[left]  # 先用一个变量来保存基数的值及4
    low = left
    high = right
    while left < right:
        # 从数组的最后向前遍历，如果发现L[right]有小于4的，就使L[left]=L[right],否则right-1
        while left < right and L[left] < L[right]:
            right -= 1
        L[left] = L[right]
        # 再从数组前向后遍历，找到大于基数的值，L[right] = L[left]，否则left+1
        while left < right and L[left] <= L[right]:
            left += 1
        L[right] = L[left]
    L[right] = key
    qk_sort(L, low, left - 1)
    qk_sort(L, left + 1, high)


# 快速排序方法二：
def quick_sort(L):
    lenth = len(L)  # 获得L的长度
    if lenth <= 1:  # 当长度小于1时 返回L
        return L
    temi = random.randint(0, lenth - 1)
    tem = L[temi]  # 随机找一个基准数
    left = []
    right = []
    for i in range(0, lenth):
        if L[i] > tem:  # 将小于基准数的放在left列表中
            right.append(L[i])
        else:
            left.append(L[i])  # 将大于tem的值放在right列表中
    return quick_sort(left) + quick_sort(right)  # 遍历 拼接


# 快速排序：取出列表中最小的k个数， 有可能出错。
'''
方法一：时间复杂度为：O(n^^2)
'''


def qk_sort2(L, left, right):
    if left >= right:
        return L
    key = L[left]  # 先用一个变量来保存基数的值及4
    low = left
    high = right
    while left < right:
        # 从数组的最后向前遍历，如果发现L[right]有小于4的，就使L[left]=L[right],否则right-1
        while left < right and L[left] < L[right]:
            right -= 1
        L[left] = L[right]
        # 再从数组前向后遍历，找到大于基数的值，L[right] = L[left]，否则left+1
        while left < right and L[left] <= L[right]:
            left += 1
        L[right] = L[left]
    L[right] = key
    qk_sort(L, low, left - 1)
    qk_sort(L, left + 1, high)


def find_k_nums(alist, k):
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return None
    left = 0
    right = length - 1
    qk_sort(alist, left, right)
    return alist[:k]


'''堆排序（nlgn）：采用二叉树排序。
首先构建大顶堆（所有父节点大于等于子节点）或小顶堆（所有子节点小于等于父节点）
以大顶堆为例，每次将顶点交换到最后，构成一个新序列，之前的堆重新调整为大顶堆，
直到所有元素都进入新序列'''
# def heapAdjust(arry,start,size): #大顶堆的调整
#     i=start
#     l=size
#     child1=2*i+1 #i的左子节点
#     child2=2*i+2 #i的右子节点
#     if start<=l/2: #只需要扫描非叶节点
#       if child1<l and arry[child1]>arry[i]:
#          i=child1
#          if child2 < l and arry[child2] > arry[i]:
#             i=child2
#        # 比较父节点和子节点，把三个节点中最大的放到父节点
#        if i!=start:
#           arry[start],arry[i]=arry[i],arry[start]
#           heapAdjust(arry,i,l)
#     return  arry
# def heapBuild(arry):  #建立大顶堆
#     size=len(arry)
#     l=int(size/2)
#     for i in range(0,l)[::-1]: #从最下层的非叶节点开始往上推
#       heapAdjust(arry,i,size)
#     return arry
# def heapSort(arry):  #大顶堆的排序
#     size=len(arry)
#     l=size-1
#     heapBuild(arry)
#     #交换首尾元素形成两个分区
#     for i in range(0,size)[::-1]:
#       arry[0],arry[i]=arry[i],arry[0]
#       #对第一个分区重新调整成大顶堆
#       heapAdjust(arry,0,i)
#     return arry


if __name__ == '__main__':
    # print(insert_sort(L))
    # print(bub_sort(L))
    # print(sel_sort(L))
    # print(bubble_sort(L))
    # print(qk_sort(L,0,len(L)-1))
    a = getrandata(10)
    # print(a)
    b = quick_sort(a)
    print(b)

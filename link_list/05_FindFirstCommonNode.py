# coding:utf-8

# 思路：
# 第一种情况：相同长度有交点
# 两个指针一起走，步长一致，碰到第一个相同的节点 p1 == p1，退出循环，return p1。
# 第二种情况：相同长度无交点
# 两个指针一起走，直到走到最后一个节点，p1.next 和 p2.next都为 None，满足 相等的条件，退出循环，return p1。
# 第三种情况：不同长度有交点
# 两个指针一起走，当一个指针p1走到终点时，说明p1所在的链表比较短，让p1指向另一个链表的头结点开始走，直到p2走到终点，让p2指向短的链表的头结点，那么，接下来两个指针要走的长度就一样了，变成第一种情况。
# 第四种情况：不同长度无交点
# 两个指针一起走，当一个指针p1走到终点时，说明p1所在的链表比较短，让p1指向另一个链表的头结点开始走，直到p2走到终点，让p2指向短的链表的头结点，那么，接下来两个指针要走的长度就一样了，变成第二种情况

"""
两个链表的第一个公共节点
题目描述
输入两个链表，找出它们的第一个公共结点
"""


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SigleLinkList:

    def FindFirstCommonNode(self, pHead1, pHead2):
        # 方法1：
        list1 = []
        while pHead1:
            list1.append(pHead1.elem)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2.elem in list1:
                return pHead2.elem
            pHead2 = pHead2.next
        return None
        # 有待验证2：
        # p1 = pHead1
        # p2 = pHead2
        # while p1 != p2:
        #     p1 = pHead2 if p1 is None else p1.next
        #     p2 = pHead1 if p2 is None else p2.next
        # return p1



if __name__ == "__main__":
    p1 = Node(9)
    p2 = Node(3)
    p3 = Node(4)
    p4 = Node(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    c1 = Node(2)
    c2 = Node(8)
    c3 = Node(4)
    c4 = Node(0)
    c1.next = c2
    c2.next = c3
    c3.next = c4
    s1 = SigleLinkList()
    print(s1.FindFirstCommonNode(p1,c1))

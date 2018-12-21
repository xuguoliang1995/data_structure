# coding:utf-8
# 判断一个链表是否有环。
# 判断一个链表是否存在环：例如n1->n2->n3->n4->n5->n6->n2就是一个有环的链表，环的开始结点是n6。
# 错误做法：
# 遍历链表，将遍历过的结点放在一个字典中，如果一个结点已经存在字典中，说明有环
# 个人认为这种方法不可行，因为如果链表中如果有重复的元素，但是重复的元素的地址是不一样的，此时并没有形成环。所以这种判断环的方法不可行。
# 正确做法
# 用快慢指针的方法。时间复杂度O(n)，空间复杂度O(1)。
# 设置p1为慢指针，p2为快指针，两者初始时都指向链表的头结点 ，慢指针p1每次前进1步，
# 快指针p2每次前进2步。如果链表存在环，则快指针p2肯定先进入环，慢指针p1后进入环，两个指针必定会相遇。如果不存在环，则快指针会先行到达链表的尾部变为None。
# 中间隔几个节点会慢慢逼近，从隔n隔变为n-1，n-2, ....1, 0 但两个节点相距0个的时候，下一步一定回相遇。
# p2每次走三步以上，并不总能加快检测的速度,反而有可能判别不出有环


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = node

    # 判断是否有环。
    def has_cricle(self):
        fast = slow = self._head
        # 当节点为空节点或者到达尾节点的时候退出循环。
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # 找环的入口
    # 一个从相交的地方走，一个从头走，当相遇的时候，这个相遇的节点就是入口
    def circlestart(self):
        # 先判断有无环。
        # fast = slow = self._head
        # # 默认环是没有的
        # flag = False
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     # 相交的地方不一定是环开始的地方。
        #     if fast == slow:
        #         flag = True
        #         break
        # # slow从头开始。
        # if flag:
        #     slow = self._head
        #     print("环的相交点为:", fast.elem)
        #     while fast != slow:
        #             fast = fast.next
        #             slow = slow.next
        #     return ("环开始的地方为% s") % fast.elem
        # return "不是环结构"

        # 更为简介的写法
        try:
            slow = self._head.next
            # 如果此时有异常一定是只有一个节点，说明不能够形成环环路。
            fast = self._head.next.next
            while fast != slow:
                slow = slow.next
                fast = fast.next.next
            h = self._head
            while h != fast:
                h = h.next
                fast = fast.next
            return h.elem
        except:
            return None


    # 访问中间的节点。
    # 这个的思想大致也就是一个一次走两步，一个一次走一步，当快的走的最后的时候，慢的在中间
    def midoflist(self):
        fast = slow = self._head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.elem)


if __name__ == '__main__':
    p1 = Node(2)
    p2 = Node(3)
    p3 = Node(4)
    p4 = Node(5)
    p5 = Node(6)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p2
    ll = SingleLinkList(p1)
    # print(ll.has_cricle())
    print(ll.circlestart())

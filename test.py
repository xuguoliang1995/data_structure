# coding:utf-8

class Node(object):
    """结点"""
    def __init__(self, prev, next, value):
        self.value = value
        self.next = next
        self.prev = prev
class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def remove(self, head, x):
        """删除节点"""
        cur = self.__head
        while cur != None:
            # 删除和x或者head相同的元素。
            if cur.value == x or cur.value == head:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 判断是否还有后续节点。
                    if cur.next:
                        cur.next.prev = cur.prev
                # 返回头部元素。
                return cur.next.value
            else:
                cur = cur.next

class Deque(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列中添加一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """往队列中添加一个item元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从队列头部删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)
# 判断是不是一个回文数
def isPalindrome(checking_string):
    dequeue = Deque()
    for ch in checking_string:
        dequeue.add_front(ch)
    while dequeue.size() > 1:
        head_char = dequeue.pop_front()
        end_char = dequeue.pop_rear()
        if head_char != end_char:
            return False
    # 列标为空或者只剩一个元素时，为回文序列，返回true
    return True

if __name__ == "__main__":
    s = Deque()
    s.add_front(1)
    s.add_rear(3)
    s.add_rear(4)
    print(s.is_empty())
    print(s.pop_rear())
    word_list = ['random', 'carrac', 'doooood', 'slefles']
    for word in word_list:
        print("%s ---- %s" % (isPalindrome(word), word))
        print("-----------------")




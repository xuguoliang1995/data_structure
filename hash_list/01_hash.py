#coding: utf-8
# 哈希表
# 哈希查找是一种以O(1)时间复杂为目标的查找方式，效率极高。Python中的内置的字典结构dictionary，其key值的查找就是采用了哈希查找的方式，因而查询操作能够达到O(1)的时间复杂度。
# 【Python】（四）Python中的字典
# 哈希表的构造原则可以总结为一下几点：

# 哈希表中项的个数最好为质数，这有利于冲突后的重新散列。
# 散列函数应最大限度的减少“冲突”发生。
# 在以开放寻址的方式解决冲突问题的同时，也应尽量避免“堆积”问题。
# 当冲突大量发生时，开放寻址的时间成本将越来越高。此时更适合使用链接解决冲突。

# 用哈希表实现字典
# 下面我们尝试基于哈希表使用python来实现简单的“字典”结构：

# 我们将哈希表的长度设定为素数13。
# 哈希函数选择平方取中法和余数法相结合的方式，具体为：将key作为字符串看待，将每个字符的ASCII值相加再平方，所得的结果取中间三位数，最后再将其除以13，所得的余数即为哈希值。
# 重新散列函数采用向前间隔为3的线性探测。

class MyDictionary(object):
      def __init__(self):
          self.table_size = 13
          self.key_lsit = [None] * self.table_size
          self.value_list = [None] * self.table_size
      def hashfuction(self, key):
          count_char = 0
          key_string = str(key)
          for key_char in key_string:
              count_char += ord(key_char)
          length = len(str(count_char))
          if length > 3:
              mid_int = 100 * int((str(count_char)[length // 2 - 1])) \
                        + 10 * int((str(count_char)[length // 2])) \
                        + 1 * int((str(count_char)[length // 2 + 1]))




      def __getitem__(self, item):
          pass





































































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


# 有可能回出错。
def qk_sort(L):
    length = len(L)
    if length <= 1:
        return L
    temp = random.randint(0, length - 1)
    tem = L[temp]
    left = []
    right = []
    for i in range(0, length):
        if L[i] > tem:
            right.append(L[i])
        else:
            left.append(L[i])
    return qk_sort(left) + qk_sort(right)


if __name__ == '__main__':
    a = getrandata(10)
    print(a)
    b = qk_sort(a)
    print(b)







#作业1
'''
(1)容器序列：list、tuple、collections.deque
   扁平序列：str
(2)可变序列：list,collections.deque
   不可变序列：tuple,str
'''

#作业2
from collections import Iterable

def Self_defined_map(func, iterable_object): 
    if isinstance(iterable_object, Iterable): #判断类型
        i = 0
        n = len(iterable_object)
        res = list(range(n))
        for z in iterable_object:
            res[i] = func(z)
            i += 1
        return res
    else:
        raise TypeError(f'{iterable_object}是不可迭代对象')

def square(x):
    return x**2

#测试用例
print(Self_defined_map(square,[1,3,5,7])) # 输出结果：[1,9,25,49]
print(Self_defined_map(square,1234)) # 输出结果：TypeError: 1234是不可迭代对象




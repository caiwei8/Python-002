#作业3
import time
import random

def timer(func):
    def get_time(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f'程序运行时间为：{run_time}')
    return get_time


@timer
def test(n):
    time.sleep(n)


if __name__ == '__main__':
    test_time = random.randint(0, 10)
    print(f'测试时间：{test_time}')
    test(test_time)

'''
题目:找出数组中重复的数字

在长度为n的数组里所有数字都在0~n-1的范围内，某些数字重复，输出一个重复的数字

输入：{2，3，1，0，2，5，3}
输出：2 或 3

'''

data = [2, 3, 1, 0, 2, 5, 3]


def findDuplication(data: list):
    for i in range(len(data)):
        while i != data[i]:
            if data[i] == data[data[i]]:
                print(data[i])
                break
            temp = data[data[i]]
            data[data[i]] = data[i]
            data[i] = temp
    print(data)


findDuplication(data)


'''
题目2:不修改数组找出重复的数字

在长度为n+1的数组里所有数字都在1~n的范围内，某些数字重复，输出一个重复的数字

输入：{2,3,5,4,3,2,6,7}
输出：2 或 3

'''
data = [2, 3, 5, 4, 2, 6, 7]


def mainprocess(data):
    start = 1
    end = len(data)-1

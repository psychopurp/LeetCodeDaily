
N = int(input())
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
M = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']


def check(num: str):
    '''检查前17位是否全为数字且最后1位校验码计算准确'''
    z = 0
    for i in range(len(num) - 1):
        if '0' <= num[i] <= '9':
            z = z + int(num[i]) * weight[i]
        else:
            return False
    z = z % 11
    if M[z] == num[-1]:
        return True
    else:
        return False


result = []
for i in range(N):
    num = input()
    if not check(num):
        result.append(num)

if len(result) == 0:
    print('All passed')
else:
    for i in result:
        print(i)
# a, b = map(int, input().split())
# lst = list(range(a, b + 1))
# print(lst)

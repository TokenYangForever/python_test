def findMinAndMax(L):
    if len(L) == 0:
      return (None, None)
    minVal = L[0]
    maxVal = L[0]
    for val in L:
      minVal = min(val, minVal)
      maxVal = max(val, maxVal)
    return (minVal, maxVal)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
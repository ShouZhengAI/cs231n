import numpy as np

arr = np.array([3, 1, 25, 10])
res = np.argsort(arr)

print("原数组:", arr)
print("索引结果:", res)
print("根据索引还原有序数组:", arr[res])

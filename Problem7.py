import random
import time

def counting_sort(arr):
    if not arr: return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output

def radix_sort(arr):
    if not arr: return []
    max_val = max(arr)
    exp = 1
    output = [0] * len(arr)
    while max_val // exp > 0:
        count = [0] * 10
        for i in range(len(arr)):
            index = (arr[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(len(arr) - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        for i in range(len(arr)):
            arr[i] = output[i]
        exp *= 10
    return arr

# 生成 100 萬個 16-bit integer (0 ~ 65535)
data = [random.randint(0, 65535) for _ in range(1_000_000)]

# 1. 測試 Python 內建 sorted()
start = time.time()
sorted(data)
print(f"Built-in sorted (Timsort): {time.time() - start:.4f} sec")

# 2. 測試自實作 Counting Sort
start = time.time()
counting_sort(data)
print(f"Counting Sort (Pure Python): {time.time() - start:.4f} sec")

# 3. 測試自實作 Radix Sort
# 複製一份資料以免 inplace 修改影響
data_copy = data.copy() 
start = time.time()
radix_sort(data_copy)
print(f"Radix Sort (Pure Python): {time.time() - start:.4f} sec")
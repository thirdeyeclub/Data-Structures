# 100
# 44 33
# 43,42 of 44 & 15 , 23 of 33
# 40,38 of 43 & 11,9 of 42 & 10,2 of 15 & None,1 of 23
# heap math
arr = [100, 44, 33, 43, 42, 15, 23, 40, 38, 11, 9, 10, 2, 1]

# left = 2*arr[i] + 1

def left(arr, index):
    return arr[index^2 +1]

print(left(arr, 3))

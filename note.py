
# Merge M Sorted Lists of Variable Length
# Given M sorted lists of variable length, print them out in sorted order efficiently.

Examples
Input: Four sorted lists of variable length

[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]

Output: 10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 40, 48, 93

    # while index > 0:
    #   #compare to parent
    #   parent = (index -1)//2
      
    #   if self.storage[index] > self.storage[parent]:
    #     self.storage[index] , self.storage[parent] = self.storage[parent] , self.storage[index]
    #     index = parent
    #   else: 
    #     break

def sort_arr(arr): 
#
#
#
#找最大的满足check的数
def binary_search(check, low, high):
    ans = None

    while low <= high:
        mid = low + (high - low) // 2

        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
#找最小的满足check的数
def binary_search(check, low, high):
    ans = None

    while low <= high:
        mid = low + (high - low) // 2

        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


#找排序好的数组中严格小于r的最大数字（不存在返回-1）
def find_smallthan_r(ls1,r):
    low,high=0,len(ls1)-1
    ans=-1
    while low <= high:
        mid = low + (high - low) // 2
        v=ls1[mid]
        if v<r:
            ans=v
            low = mid + 1
        else:
            high = mid - 1
    return ans

#找排序好的数组中严格大于l的最小数字（不存在返回10**9）
def find_bigthan_l(ls2,l):
    low,high=0,len(ls2)-1
    ans=10**9
    while low <= high:
        mid = low + (high - low) // 2
        v = ls2[mid]
        if v > l:
            ans = v
            high = mid - 1
        else:
            low = mid + 1
    return ans
#print(find_bigthan_l([1,2,3,3,4,6,7],3))
def find_min_in_array(arr):
    left, right = 0, len(arr) - 1  # 注意这里的right初始化为len(arr) - 2

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:  # 如果mid的元素大于它右边的元素
            right = mid  # 最小值在mid及其右边
        else:
            left = mid + 1  # 最小值在mid及其左边

    # 最后，left和right会在最小值的位置相遇
    return left, arr[left]

# 示例
arr = [3, 2, 1, 1, 1, 3, 4, 5]
index_of_min, min_value = find_min_in_array(arr)
print(f"The index of the minimum value is: {index_of_min}")
print(f"The minimum value is: {min_value}")
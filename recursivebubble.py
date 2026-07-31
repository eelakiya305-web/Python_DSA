

class Solution:
    def bubbleSort(self, nums):
        def bubble(arr, j, n):
            if j == n - 1:
                return
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            bubble(arr, j + 1, n)

        def sort(arr, n):
            if n == 1:
                return
            bubble(arr, 0, n)
            sort(arr, n - 1)

        sort(nums, len(nums))
        return nums
nums = list(map(int, input().split()))
ob=Solution()
print(ob.bubbleSort(nums))
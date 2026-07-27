class Solution:
    def selectionSort(self, arr):
        n=len(arr)
        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr
arr=[5,3,6,9,0,1,6]
ob=Solution()
print(ob.selectionSort(arr))
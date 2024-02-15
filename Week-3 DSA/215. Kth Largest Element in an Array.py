class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def build_min_heap(arr, k):
            for i in range(k // 2 - 1, -1, -1):
                min_heapify(arr, i, k)

        def min_heapify(arr, i, size):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < size and arr[left] < arr[smallest]:
                smallest = left
            if right < size and arr[right] < arr[smallest]:
                smallest = right

            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                min_heapify(arr, smallest, size)

        def find_kth_largest(arr, k):
            build_min_heap(arr, k)

            for i in range(k, len(arr)):
                if arr[i] > arr[0]:
                    arr[i], arr[0] = arr[0], arr[i]
                    min_heapify(arr, 0, k)

            return arr[0]

        return find_kth_largest(nums, k)

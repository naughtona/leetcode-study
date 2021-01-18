from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap
        count = Counter(nums)

        # ## heap approach
        # # build heap of top k frequent elements
        # # convert to output array
        # # O(n log k) time
        # return heapq.nlargest(k, count.keys(), key=count.get)

        # ## bucket sort idea
        # buckets = [[] for _ in range(len(nums))]
        # for num, freq in count.items():
        #     buckets[freq-1].append(num)
        # res = []
        # i = len(buckets) - 1
        # while i >= 0 and k > 0:
        #     j = 0
        #     while j < len(buckets[i]) and k > 0:
        #         res.append(buckets[i][j])
        #         k -= 1
        #         j += 1
        #     i -= 1
        # return res

        ## Quickselect and hoare's partition
        unique = list(count.keys())
        n = len(unique)
        
        def quickselect(left, right, target):
            def partition(l, r, pivot):
                i = store_index = l

                while i < r:
                    if count[unique[i]] < count[unique[pivot]]:
                        unique[store_index], unique[i] = unique[i], unique[store_index]
                        store_index += 1
                    i += 1

                unique[store_index], unique[pivot] = unique[pivot], unique[store_index]

                return store_index

            if left == right:
                return

            pivot = partition(left, right, right) # pivot is right element

            if pivot == target:
                return
            elif pivot > target:
                return quickselect(left, pivot-1, target)
            else:
                return quickselect(pivot+1, right, target)
        
        quickselect(0, n-1, n-k)
        return unique[n-k:]


# >>> from top_k_frequent_elements import Solution
# >>> Solution().topKFrequent([1,1,1,2,2,3],2)
# [1, 2]
# >>> Solution().topKFrequent([1],1)
# [1]
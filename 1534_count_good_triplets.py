from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res, n = 0, len(arr)
        for i in range(n):
            for j in range(i+1, n):
                if abs(arr[i] - arr[j]) <= a:   
                    for k in range(j+1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            res += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))
    print(solution.countGoodTriplets([1,1,2,2,3], 0, 0, 1))
    print(solution.countGoodTriplets([7,3,7,3,12,1,12,2,3], 5, 8, 1))

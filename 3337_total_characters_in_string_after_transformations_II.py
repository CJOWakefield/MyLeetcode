from typing import List
import numpy as np
import time

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9 + 7
        frequencies = [0] * 26
        for char in s: frequencies[ord(char) - ord('a')] += 1
        for _ in range(t):
            freq_adjusted = [0] * 26
            for pos in range(26): 
                curr = frequencies[pos]
                if curr > 0:
                    for i in range(nums[pos]): freq_adjusted[(pos + i + 1) % 26] += curr
            frequencies = freq_adjusted
        return sum(frequencies) % mod

    # Implementation with matrix exponentiation, in place of iterative transformation.
    def lengthAfterTransformations_II(self, s: str, t: int, nums: List[int]) -> int:
        
        def transformation_matrix(nums):
            matrix = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(nums[i]):
                    matrix[i][(i + j + 1) % 26] = 1
            return matrix
        
        def matrix_multiply(a, b):
            result = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % mod
            return result
        
        def matrix_exponentiation(matrix, power):
            result = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            while power > 0:
                if power % 2 == 1:
                    result = matrix_multiply(result, matrix)
                matrix = matrix_multiply(matrix, matrix)
                power //= 2
            return result

        mod = 10**9 + 7
        frequencies, trans_matrix = [0] * 26, transformation_matrix(nums)
        exp_matrix = matrix_exponentiation(trans_matrix, t)
        for char in s: frequencies[ord(char) - ord('a')] += 1

        res = [0] * 26
        for i in range(26):
            for j in range(26):
                res[j] = (res[j] + frequencies[i] * exp_matrix[i][j]) % mod
        return sum(res) % mod
    
    # Attempted implementation with NumPy, success but % not applied where required in process -> incorrect larger solutions.
    def lengthAfterTransformations_III(self, s: str, t: int, nums: List[int]) -> int:

        def matrix_exp(matrix, power, mod):
            result = np.eye(26, dtype=int)
            while power > 0:
                if power % 2 == 1:
                    result = np.matmul(result, matrix) % mod
                matrix = np.matmul(matrix, matrix) % mod
                power //= 2
            return result
        
        mod = 10 ** 9 + 7
        trans_matrix = np.zeros((26, 26), dtype=int)
        for i in range(26):
            for j in range(nums[i]):
                trans_matrix[i, (i + j + 1) % 26] = 1
    
        trans_matrix = matrix_exp(trans_matrix, t, mod)   
        frequencies = np.zeros(26, dtype=int)
        for char in s: frequencies[ord(char) - ord('a')] += 1
        res = np.dot(frequencies, trans_matrix) % mod
        return sum(res) % mod
    
    
    
if __name__ == "__main__":
    sol = Solution()
    start_time = time.time()
    print(sol.lengthAfterTransformations("abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
    print(sol.lengthAfterTransformations("azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    
    start_time = time.time()
    print(sol.lengthAfterTransformations_II("abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
    print(sol.lengthAfterTransformations_II("azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    print(sol.lengthAfterTransformations_III("abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
    print(sol.lengthAfterTransformations_III("azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

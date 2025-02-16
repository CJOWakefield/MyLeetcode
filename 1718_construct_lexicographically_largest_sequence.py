class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        res = [0] * (2 * n - 1)
        used = set()

        def backtrack(pos):
            if pos == 2 * n - 1: return True
            if res[pos] != 0: return backtrack(pos+1)
            
            for i in range(n, 0, -1):
                if i in used: continue
                if i > 1:
                    if (pos+i) >= len(res) or res[pos+i] != 0: continue
                    res[pos] = res[pos+i] = i
                    used.add(i)
                    if backtrack(pos+1): return True

                    res[pos] = res[pos+i] = 0
                    used.remove(i)
                
                else:
                    res[pos] = i
                    used.add(i)
                    if backtrack(pos+1): return True

                    res[pos] = 0
                    used.remove(i)
                
            return False
        
        backtrack(0)
        return res
    
# Step-by-step explanation:
# 1. Problem Setup:
#    - Given a number n, we need to create an array of length 2n-1
#    - Each number from 1 to n must appear exactly once, except n appears twice
#    - For any number i > 1, its two occurrences must be exactly i positions apart
#    - Need to find lexicographically largest valid sequence

# 2. Initialization:
#    - Create array 'res' of length 2n-1 filled with zeros
#    - Create empty set 'used' to track which numbers we've placed
#    - Start backtracking from position 0

# 3. Backtracking Function:
#    - Base case: if we reach end of array (pos == len(res)), we found valid solution
#    - If current position is filled, skip to next position
#    - Try numbers from n down to 1 (ensures lexicographically largest)

# 4. Number Placement Rules:
#    For numbers > 1:
#    - Check if number is already used
#    - Check if pos + num is within array bounds
#    - Check if second position (pos + num) is empty
#    - Place number at both positions
#    For number 1:
#    - Just place at current position if not used

# 5. Backtracking Process:
#    - If placement leads to valid solution, keep it
#    - If not, undo the placement:
#      * Remove number from position(s)
#      * Remove from used set
#      * Try next number

# 6. Time and Space Complexity:
#    Time: O(n!) in worst case, but much faster in practice due to pruning
#    Space: O(n) for array and used set, plus O(n) for recursion stack

# 7. Key Optimizations:
#    - Using set for O(1) lookup of used numbers
#    - Trying largest numbers first for lexicographical order
#    - Early termination when valid solution found
#    - Skipping filled positions automatically
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.constructDistancedSequence(5))
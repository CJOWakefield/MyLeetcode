import re

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        min_replace = re.search(r'[1-9]', num_str)
        max_replace = re.search(r'[0-8]', num_str)

        min_val = int(num_str.replace(num_str[min_replace.start()], '0')) if min_replace else num
        max_val = int(num_str.replace(num_str[max_replace.start()], '9')) if max_replace else num

        return max_val - min_val
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.minMaxDifference(11891))
    print(solution.minMaxDifference(90))
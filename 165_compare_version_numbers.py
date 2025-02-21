import time

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version_1, version_2 = version1.split('.'), version2.split('.')
        for i in range(max(len(version_1), len(version_2))):
            val_1 = int(version_1[i]) if i < len(version_1) else 0
            val_2 = int(version_2[i]) if i < len(version_2) else 0
            if val_1 > val_2: return 1
            elif val_1 < val_2: return -1
        return 0


if __name__ == "__main__":
    problem = Solution()
    print(problem.compareVersion("1.01", "1.001"))
    print(problem.compareVersion("1.0", "1.0.0"))
    print(problem.compareVersion("0.1", "1.1"))
    
    
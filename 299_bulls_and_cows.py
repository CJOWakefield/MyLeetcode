from collections import Counter, defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_counts = Counter(secret)
        rems, bulls, cows = defaultdict(int), 0, 0
        for i, char in enumerate(guess):
            if char == secret[i]: 
                bulls += 1
                secret_counts[char] -= 1
            elif secret_counts[char] > 0: 
                rems[char] += 1
            else: continue

        for rem in rems:
            cows += min(rems[rem], secret_counts[rem])
        return f'{bulls}A{cows}B'
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.getHint("1807", "7810"))
    print(problem.getHint("1123", "0111"))
    
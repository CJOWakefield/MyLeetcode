class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        res = 1
        for i in range(len(self.requests)-2, -1, -1):
            if t - self.requests[i] <= 3000: res += 1
            else: return res
        return res


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == '__main__':
    problem = RecentCounter()
    print(problem.ping(1))
    print(problem.ping(100))
    print(problem.ping(3001))
    print(problem.ping(3002))
    
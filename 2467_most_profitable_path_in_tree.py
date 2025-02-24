class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n, res = len(edges)+1, float('-inf')
        times_bob = [n] * n

        connections = [[] for _ in range(n)]
        for i, j in edges:
            connections[i].append(j)
            connections[j].append(i)
        
        def dfs_bob(node, prev, time):
            if node == 0: 
                times_bob[node] = time
                return True
            for sub_node in connections[node]:
                if sub_node != prev and dfs_bob(sub_node, node, time+1):
                    times_bob[node] = time
                    return True
            return False
        
        def dfs_alice(node, prev, time, profit):
            curr_profit = profit
            if time < times_bob[node]:
                curr_profit += amount[node]
            elif time == times_bob[node]:
                curr_profit += amount[node] // 2
            
            if len(connections[node]) == 1:
                nonlocal res
                res = max(res, curr_profit)
                return
            
            for sub_node in connections[node]:
                if sub_node != prev:
                    dfs_alice(sub_node, node, time+1, curr_profit)
        
        dfs_bob(bob, -1, 0)
        connections[0].append(-1)
        dfs_alice(0, -1, 0, 0)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]))
    print(sol.mostProfitablePath([[0,1],[1,2],[1,3],[3,4],[3,5]], 3, [20,10,30,40,10,20]))

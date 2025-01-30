def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    root = list(range(len(edges)+1))

    def root_find(node):
        if root[node] != node: root[node] = root_find(root[node])
        return root[node]

    for e1, e2 in edges:
        r1, r2 = root_find(e1), root_find(e2)
        if r1 == r2: return [e1, e2]
        else: root[r2] = r1

if __name__ == '__main__':
    print(findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))

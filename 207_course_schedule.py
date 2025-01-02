from collections import defaultdict, deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    res = []
    reqs = defaultdict(set)
    dependents = defaultdict(int)

    for i in range(numCourses): dependents[i] = 0
    for pre in prerequisites:
        reqs[pre[1]].add(pre[0])
        dependents[pre[0]] += 1

    to_search = deque([course for course in dependents if dependents[course] == 0])
    while to_search:
        curr = to_search.popleft()
        res.append(curr)
        for req in reqs[curr]:
            dependents[req] -= 1
            if dependents[req] == 0:
                to_search.append(req)

    return len(res) == numCourses

if __name__ == '__main__':
    print(canFinish(2, [[1,0],[0,1]]))

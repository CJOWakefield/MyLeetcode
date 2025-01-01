from collections import defaultdict, deque

def CourseScheduleII(numCourses, prerequisites):
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

    return res

if __name__ == '__main__':
    print(CourseScheduleII(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))

import time

def hIndex(citations: list[int]) -> int:
    left, right = 0, len(citations)
    while left <= right:
        mid = right - left // 2
        curr = list(filter(lambda x: x>=mid, citations))
        if len(curr) >= mid:
            left = mid+1
        else:
            right = mid-1
    return mid

# Notes: No real issues, intuitive solution by binary search. Only point for improvement - sort list before search but current solution clean.

if __name__ == '__main__':
    print(hIndex([3,0,6,1,5]))

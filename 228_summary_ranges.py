def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    ranges = []
    for n in nums:
        if ranges and ranges[-1][1] == n-1:
            ranges[-1][1] = n
        else:
            ranges.append([n, n])

    return  [f'{r[0]}->{r[1]}' if r[0] != r[1] else f'{r[0]}' for r in ranges]

# Notes: Had a lot of issues with this actually. Approach of adjusting the last value in the last tuple of range makes sense. Just an issue of being unable to work out the logic.

if __name__ == '__main__':
    print(summaryRanges([0,1,2,4,5,7]))

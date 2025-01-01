from collections import Counter

def majorityElement(nums: list[int]) -> int:
    counter = Counter(nums)

    for key in counter.keys():
        if counter[key] >= len(nums) / 2:
            return key


if __name__ == '__main__':
    print(majorityElement([2, 3, 2, 2, 3, 4, 2, 1, 2, 3]))

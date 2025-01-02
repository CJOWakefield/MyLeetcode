from collections import defaultdict

def majorityElement(nums: list[int]) -> list[int]:
    tallys = defaultdict(int)
    for num in nums:
        tallys[num] += 1
    return [key for key, val in tallys.items() if val > len(nums) / 3]

if __name__ == '__main__':
    print(majorityElement([1, 1, 3, 2, 1, 1, 1, 3, 5, 7, 8, 10, 15]))

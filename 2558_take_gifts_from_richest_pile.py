import heapq
import math

def pickGifts(gifts: list[int], k: int) -> int:
    res = []
    heapq.heapify(res)
    for gift in gifts: heapq.heappush(res, -gift)
    for _ in range(k):
        gift = heapq.heappop(res)
        heapq.heappush(res, -math.floor(math.sqrt(-gift)))
    return -sum(res)

if __name__ == '__main__':
    print(pickGifts(gifts = [25,64,9,4,100], k = 4))

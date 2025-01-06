def mincostTickets(days: list[int], costs: list[int]) -> int:
    day_costs = [0 for _ in range(max(days)+1)]
    for i in range(1, len(day_costs)):
        if i not in days: day_costs[i] += day_costs[i-1]
        else:
            cost_p1 = day_costs[i-1] + costs[0]
            cost_p2 = day_costs[max(0, i-7)] + costs[1]
            cost_p3 = day_costs[max(0, i-30)] + costs[2]
            day_costs[i] = min(cost_p1, cost_p2, cost_p3)
    return day_costs[-1]

if __name__ == '__main__':
    print(mincostTickets([1,4,6,7,8,20], [9,38,134]))

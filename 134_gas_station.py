def canCompleteCircuit(gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(gas)):
            nxt = i+1
            petrol = gas[i]
            print(f'Starting position: {i} --- starting fuel: {petrol}')
            while petrol > 0:
                # End case, need to loop back to i == 0
                if nxt == len(gas):
                    nxt = 0
                # Success case
                if nxt == i and cost[nxt-1] <= petrol:
                    return i
                print(f'Travelling to station {nxt}: petrol = {petrol} - {cost[nxt-1]}')
                petrol -= cost[nxt-1]
                if petrol > 0:
                    petrol += gas[nxt]
                    nxt += 1
                else:
                    continue
        return -1

### Notes on first attempt - successful pattern identification, fails test cases due to time constraint. For longer inputs, time complexity too high O(n2).

def canCompleteCircuit_solution(gas, cost):
        gas_total, curr_total, start = 0, 0, 0
        for i in range(len(gas)):
            gas_total += gas[i] - cost[i]
            curr_total += gas[i] - cost[i]
            if curr_total < 0:
                start = i+1
                curr_total = 0

        return start if gas_total >= 0 else -1

# Solution notes. Rather than iteratively completing loop everytime, attempt start pos, if fail, move to next. Aggregate total petrol accumulated throughout the loop from i=0 to i=n.
# If we have excess petrol by end of loop, we must be able to reach that postion from the end as the cumulative total exceeds the cost.

if __name__ == '__main__':
    print(canCompleteCircuit([3,1,1], [1,2,2]))
    # print(res)

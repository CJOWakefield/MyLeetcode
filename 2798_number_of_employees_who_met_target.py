def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
    return len([hour for hour in hours if hour >= target])

# Notes: Piece of piss. No idea why this would be a question asked by Amazon.

if __name__ == '__main__':
    print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))

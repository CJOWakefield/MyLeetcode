from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        self.bookings = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        pos = self.bookings.bisect_right(startTime)
        if pos < len(self.bookings):
            if endTime > self.bookings.keys()[pos]:
                return False

        if pos > 0:
            if self.bookings.values()[pos-1] > startTime:
                return False

        self.bookings[startTime] = endTime
        return True

if __name__ == '__main__':
    myCal = MyCalendar()
    myCal.book(10, 20)
    myCal.book(15, 25)
    myCal.book(20, 30)
    print(myCal.bookings)

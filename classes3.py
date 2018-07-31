# delay the flight.

class flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def printInfo(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

    def delay(self, amount):
        self.duration += amount

def main():

    # create flight.
    f1 = flight(origin = "Khulna", destination = "Macca", duration = 540)
    f1.delay(10)
    f1.printInfo()

if __name__ == "__main__":
    main()

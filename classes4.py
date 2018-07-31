# allPassengers. multiple classes.

class flight:

    counter = 1
    def __init__(self, origin, destination, duration):

        # keep track of id number.
        self.id = flight.counter
        flight.counter += 1

        # keep track of allPassengers.
        self.allPassengers = []

        # details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def printInfo(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("allPassengers: ")
        for passenger in self.allPassengers:
            print(f"{passenger.name}")

    def delay(self, amount):
        self.duration += amount

    def addPassenger(self, p):
        self.allPassengers.append(p)
        p.flightId = self.id

class passenger:
    def __init__(self, name):
        self.name = name

def main():


    # create flight.
    f1 = flight(origin = "Khulna", destination = "Macca", duration = 540)

    # create allPassengers.
    Shaon = passenger(name = "Shaon")
    Sujon = passenger(name = "Sujon")

    # add allPassengers.
    f1.addPassenger(Shaon)
    f1.addPassenger(Sujon)

    f1.printInfo()

if __name__ == "__main__":
    main()

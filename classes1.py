class flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

def main():

    # create flight.
    f = flight(origin = "Khulna", destination = "Macca", duration = 540)

    # chage the value of a variable.
    f.duration += 10

    # print details about flight.
    print(f.origin)
    print(f.destination)
    print(f.duration)

if __name__ == "__main__":
    main()

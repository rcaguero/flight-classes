class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.name = ""

    def display_users(self):
        print("Username:", self.username)
        print("Password:", self.password)
        print("Name:", self.name)


class Flight:
    def __init__(self):
        self.flightID = ""
        self.airline = ""
        self.source = ""
        self.destination = ""
        self.pricePerPassenger = ""

    def display_flight(self):
        print("Flight ID:", self.flightID, "// Airline:", self.airline, "// Source:", self.source, "// Destination:",
              self.destination, " // Price Per Passenger:", self.pricePerPassenger, end="")
        # print("Flight ID:", self.flightID)
        # print("Airline:", self.airline)
        # print("Source:", self.source)
        # print("Destination:", self.destination)
        # print("Price Per Passenger:", self.pricePerPassenger)


class Trip:
    def __init__(self):
        self.tripID = ""
        self.source = ""
        self.destination = ""
        self.date = ""
        self.numOfPassengers = ""
        self.totalCost = ""

    def display_trip(self):
        print("--------------------Trip Ticket-----------------")
        print("Trip ID: ", self.tripID)
        print("Source: ", self.source)
        print("Destination: ", self.destination)
        print("Date of Trip: ", self.date)
        print("Number of Passengers: ", self.numOfPassengers)
        print("Total cost: $", self.totalCost)
        print("-----------------------------------------------")

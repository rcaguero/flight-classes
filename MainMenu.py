import FlightClasses

user_list = []
flight_list = []
trip_list = []
trip_ID = 0


def load_user_details():
    fp = open("user-objects.txt", "r")
    j = 0
    for f_obj in fp:
        user_list.append("User" + str(j))
        user_list[j] = FlightClasses.User()
        array = f_obj.split("-")
        user_list[j].username = array[0]
        user_list[j].password = array[1]
        user_list[j].name = array[2]
        # user_list[j].display_users()
        j += 1


def load_flight_details():
    fp = open("flight-objects.txt", "r")
    j = 0
    for line in fp:
        array = line.split(",")

        flight_list.append("Flight" + str(j+1))
        flight_list[j] = FlightClasses.Flight()

        flight_list[j].flightID = array[0]
        flight_list[j].airline = array[1]
        flight_list[j].source = array[2]
        flight_list[j].destination = array[3]
        flight_list[j].pricePerPassenger = array[4]
        j += 1


def user_login():
    usernm = input("Please enter your username:")
    password = input("Please enter your password:")
    for i in range(0, len(user_list)):
        if usernm == user_list[i].username:
            if password == user_list[i].password:
                print("Successfully logged in")
                # Run schedule_trip here
                return True
            else:
                print("Password is not in database")
                return False


def schedule_a_trip():
    j = 0
    cost = 0
    roundOrNot = int(input("Wil this be a round-way trip? (Enter 1 if one-way, 2 if round-trip): "))
    if roundOrNot == 1:
        source = input("Enter the source of your flight: ")
        for i in range(0, len(flight_list)):
            if source == flight_list[i].source:
                dest = input("Enter your desired destination:  ")
                date = input("Enter the date of this flight: ")
                numOfPassengers = input("Enter the number of passengers in this flight: ")

                trip_list.append("Trip" + str(j))
                trip_list[j] = FlightClasses.Trip()
                trip_list[j].tripID = str(trip_ID + 1)
                trip_list[j].source = source
                trip_list[j].destination = dest
                trip_list[j].date = date
                trip_list[j].numOfPassengers = numOfPassengers
                cost = int(numOfPassengers) * int(flight_list[i].pricePerPassenger)
                trip_list[j].totalCost = str(cost)
                trip_list[j].display_trip()

                f = open("trips.txt", "w")
                print("--------------------Trip Ticket-----------------", file=f)
                print("Trip ID: ", trip_list[j].tripID, file=f)
                print("Source: ", trip_list[j].source, file=f)
                print("Destination: ", trip_list[j].destination, file=f)
                print("Date of Trip: ", trip_list[j].date, file=f)
                print("Number of Passengers: ", trip_list[j].numOfPassengers, file=f)
                print("Total cost: $", trip_list[j].totalCost, file=f)
                print("-----------------------------------------------", file=f)
                f.close()

                return "Successfully created trip."
        return "The source you are trying to leave from is not in the database."
    elif roundOrNot == 2:
        cost = 0
        source = input("Enter the source of your flight: ")
        for i in range(0, len(flight_list)):
            if source == flight_list[i].source:
                dest = input("Enter your desired destination:  ")
                date = input("Enter the date of this flight: ")
                numOfPassengers = input("Enter the number of passengers in this flight: ")

                trip_list.append("Trip" + str(j))
                trip_list[j] = FlightClasses.Trip()
                trip_list[j].tripID = str(trip_ID + 1)
                trip_list[j].source = source
                trip_list[j].destination = dest
                trip_list[j].date = date
                trip_list[j].numOfPassengers = numOfPassengers
                cost = int(numOfPassengers) * int(flight_list[i].pricePerPassenger) * 2
                trip_list[j].totalCost = str(cost)
                trip_list[j].display_trip()

                f = open("trips.txt", "w")
                print("--------------------Trip Ticket-----------------", file=f)
                print("Trip ID: ", trip_list[j].tripID, file=f)
                print("Source: ", trip_list[j].source, file=f)
                print("Destination: ", trip_list[j].destination, file=f)
                print("Date of Trip: ", trip_list[j].date, file=f)
                print("Number of Passengers: ", trip_list[j].numOfPassengers, file=f)
                print("Total cost: $", trip_list[j].totalCost, file=f)
                print("-----------------------------------------------", file=f)
                f.close()

                return "Successfully created trip."
        return "The source you are trying to leave from is not in the database."
    else:
        print("Not a valid value.")


def display_trip_history():
    if len(trip_list) == 0:
        print("There are no tickets to print.")
    else:
        print("-------------------------Ticket History---------------------------")
        for i in range(0, len(trip_list)):
            trip_list[i].display_trip()
            print("")


def flight_displayer():
    print("-------------------------------------------------------Flight Information-----------------------"
          "----"
          "----------------------")
    for i in range(0, len(flight_list)):
        flight_list[i].display_flight()
    flight_displayer.has_been_called = True


load_user_details()
load_flight_details()
while 1:
    flight_displayer.has_been_called = False
    log_in = user_login()
    if log_in:
        while 1:
            print("------------------------Flight Planner---------------------------------")
            print("(1) Display Flights")
            print("(2) Schedule a trip")
            print("(3) Display Past Ticket")
            print("(4) Exit")
            print("-----------------------------------------------------------------------")
            user_choice = int(input("Please enter a choice: "))
            if user_choice == 1:
                flight_displayer()
                print("")
            elif user_choice == 2:
                if flight_displayer.has_been_called ==  True:
                    print(schedule_a_trip())
                    trip_ID += 1
                else:
                    print("Cannot schedule a trip since flight details have not been displayed.")
            elif user_choice == 3:
                display_trip_history()
            elif user_choice == 4:
                print("Exiting program now.")
                exit(1)
            else:
                print("Not a valid option. Exiting program")
                break
    else:
        print("Log in was not successful. Please try again")




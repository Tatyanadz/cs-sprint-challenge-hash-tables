#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    flight_cache = {}

    route = []

    for ticket in tickets: 
        flight_cache[ticket.source] = ticket.destination
    
    current_flight = flight_cache["NONE"]

    while current_flight != "NONE":
        route.append(current_flight)
        current_flight = flight_cache[current_flight]
    route.append(current_flight)

    return route

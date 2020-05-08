#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    # Store in dict, where source:destination
    indices = {}
    route = []
    for i in tickets:
        indices[i.source] = i.destination
    for i in range(len(tickets)):
        if i == 0:
            route.append(indices['NONE'])
        else:
            key = route[i - 1]
            route.append(indices[key])

    return route


if __name__ == '__main__':
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]
    result = reconstruct_trip(tickets, 3)
    print(result)

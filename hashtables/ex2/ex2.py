from hashtables import (HashTable, hash_table_insert, hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # for all the the ticket in the array of given tickets
    for ticket in tickets:
        # insert into hash tables
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # get the first item for the route where key is NONE
    first_ticket = hash_table_retrieve(hashtable, 'NONE')
    # insert it into the first position on the route
    route[0] = first_ticket

    # for the rest of the space in the route
    for i in range(1, len(route)):
        # get the ticket before the next to be inserted from the route
        preceding_ticket = route[i - 1]
        # retrieve the value using the preceding ticket from the hastable
        ticket = hash_table_retrieve(hashtable, preceding_ticket)
        # insert it into postion in routes
        route[i] = ticket

    return route

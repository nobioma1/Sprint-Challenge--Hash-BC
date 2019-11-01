#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(0, length):
        current_weight = weights[i]
        hash_table_insert(ht, current_weight, i)
        diff = limit - current_weight

        value = hash_table_retrieve(ht, diff)

        if value:
            if length == 2:
                return (1, 0)
            return (i, value)

    return None
    

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

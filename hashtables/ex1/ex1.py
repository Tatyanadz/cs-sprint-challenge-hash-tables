def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    new_dict = {}

    for i in range(length):

        if limit - weights[i] in new_dict:
            k = limit - weights[i]
            i2 = new_dict[k]
            return [i, i2]
        new_dict[weights[i]] = i

    return None

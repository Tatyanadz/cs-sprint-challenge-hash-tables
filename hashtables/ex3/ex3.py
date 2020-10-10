def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    index = {}
    result = []

    for array in arrays: 
        for int in array:
            if int in index:
                index[int] += 1

                if index[int] == len(arrays):
                    result.append(int)

            else:
                index[int] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

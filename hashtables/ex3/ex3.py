def intersection(arrays):

    """
    YOUR CODE HERE
    """
    index = {}
    for arr in arrays:
        for item in arr:
            if item not in index:
                index[item] = 1
            else:
                index[item] += 1

    result = [key for key in index if index[key] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))

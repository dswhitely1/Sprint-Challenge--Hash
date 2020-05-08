def intersection(arrays):

    """
    YOUR CODE HERE
    """
    index = {}
    for i in len(arrays):
        for item in arr:
            if i == 0:
                index[item] = False
            else:
                if item in index:
                    index[item] = True
    print(index)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))

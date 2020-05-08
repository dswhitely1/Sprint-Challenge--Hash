def has_negatives(a):
    """
    YOUR CODE HERE
    """
    results = {}
    for item in a:
        if item < 0:
            # Turn Positive
            pos = item * -1
            if pos not in results:
                results[pos] = 1
            else:
                results[pos] += 1
        else:
            if item not in results:
                results[item] = 1
            else:
                results[item] += 1
    result = [key for key in results if results[key] > 1]
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

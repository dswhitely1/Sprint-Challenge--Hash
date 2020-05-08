def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Implement Hash Table
    results = {}
    # Store as total: (index1, index2)
    # Recursive Get all possible values
    def helper(arr, index=0):
        if index == len(weights):
            return
        for i in range(index+1, len(weights)):
            sum = weights[index] + weights[i]
            if sum not in results:
                if i > index:
                    results[sum] = (i, index)
                else:
                    results[sum] = (index, i)
            helper(weights, index+1)

    helper(weights)
    if limit in results:
        return results[limit]
    else:
        return None


if __name__ == "__main__":
    weights = [9]
    print(get_indices_of_item_weights(weights, 1, 9))
    weights = [4, 4]
    print(get_indices_of_item_weights(weights, 2, 8))
    weights = [4, 6, 10, 15, 16]
    print(get_indices_of_item_weights(weights, 5, 21))
    weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    print(get_indices_of_item_weights(weights, 9, 7))

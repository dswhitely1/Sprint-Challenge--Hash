def finder(files, queries):

    """
    YOUR CODE HERE
    """
    results = {}
    for file in files:
        short_name = file.split('/')[-1]
        if short_name in results:
            results[short_name].append(file)
        else:
            results[short_name] = [file]
    result = []
    for query in queries:
        if query in results:
            query_list = results[query]
            for item in query_list:
                result.append(item)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

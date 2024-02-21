def top_n(items, n):
    """Returns the top n items in an array, in descending order.

    Args:
        item(array) : list or array like object
        n(int) : the number of items to return

    Returns:
        array : the top n items in the array, in desc order

    Egs:
        >>> top_n([8, 3, 2, 7, 4], 3)
            [8, 7, 4]

    """
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j + 1]: # check if the first value is larger
                items[j], items[j + 1] = items[j + 1], items[j] # swap the two if true

    # Extract the last 3 items
    top_n = items[-n:]

    # Return in desc order
    return top_n[::-1]
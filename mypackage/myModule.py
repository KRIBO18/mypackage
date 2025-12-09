def top_n(items, n):
    """
    Return the top n items in an array, in descending order.

    Args:
    
        :Array items: list or array-like object containing numerical values.
        :int n: number of top items to return.
    Returns:
        array: top n items, in descending order.    
    """
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(item)-1-i):

            if items[j] > items[j+1]: # if this item is bigger than next item..
                items[j], items[j+1] = items[j+1], items[j] # swap the two!

    # get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]


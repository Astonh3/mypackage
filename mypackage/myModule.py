def top_n (items,n):
    """"Return top n items in an array, in desc order.

    Args:
        items (array):list or array-like object
        n(int):number of items to return

    ruturn:
        array:top n items, in desc order.

    Eg:
        >>> top_n([8,3,2,7,4],3)
        [8,7,3]
    """
    for i in range(n): #Keep sorting until we have the top 10 items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:#If his item is bigger than the next items
                items[j], items[j+1]=items [j+1],items[j]#swap the two

    # Get last two items
    top_n=items[-n:]

    #return in desc order
    return top_n[::-1]
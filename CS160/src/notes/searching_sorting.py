

def search(lst, item):
    """This is not a recursive implementation of a recursive algorithm"""
    first = 0
    last = len(lst - 1)

    found = False # False by default because that's a good idea

    while first <= last and not found:
        midpoint = (first+last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


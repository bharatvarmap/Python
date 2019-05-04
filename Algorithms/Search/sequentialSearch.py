def seqSearch(alist,b):
    length = len(alist)
    found = False
    pos = 0
    stop = False
    while pos < length and not found and not stop:
        if a[pos] == b:
            found = True
        else :
            if a[pos] > b :
                stop = True
            else:
                pos += 1

    return found

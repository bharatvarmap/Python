def binSearch(alist,b):
    found = False
    pos = 0
    first = 0
    last = len(alist) - 1

    if len(alist) == 0:
        return False

    else:
        midpoint = (first + last)//2
        if alist[midpoint] == b:
            return True
        else:
            if alist[midpoint] > b:
                return binSearch(alist[:midpoint],b)
            else:
                return binSearch(alist[midpoint+1 : ],b)

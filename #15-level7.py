def res(strok, end):
    if len(end) == 0:
        return True
    if len(end) > len(strok):
        return False
    for i in range(1, len(end)+1):
        if strok[-1] != end[-i]:
            return False
    return True

def linked_sort(a_to_sort,a_linked,key=None):
    pari = []
    for i in range(len(a_to_sort)):
        pari.append([a_to_sort[i], a_linked[i]])
    
    if key is None:
        pari.sort()
    else:
        for i in range(len(pari)):
            for j in range(len(pari) - 1):
                if key(pari[j][0], pari[j+1][0]) > 0:
                    pari[j], pari[j+1] = pari[j+1], pari[j]
            
    result = []
    for x in pari:
        result.append(x[0])
    return result

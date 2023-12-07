def ParseRow(thelist):
    array = []
    thelist = thelist.strip()
    array = thelist.split(' ')
    array = list(filter((' ').ne, array))
    array = list(filter(('').ne, array))
    return array

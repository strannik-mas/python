def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)

def area_of_disk(radius):
    '''Help on function:
        area_of_disk(number) -> number
        Return area of disk by radius
    '''
    return 3.14*radius**2

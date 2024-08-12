def same_structure_as(a, b):
    def is_list(p):
        return isinstance(p, list)
    
    if not is_list(a) and not is_list(b):
        return True
    elif (is_list(a) and is_list(b)) and (len(a) == len(b)):
        return all(map(same_structure_as, a, b)) # Here
    return False

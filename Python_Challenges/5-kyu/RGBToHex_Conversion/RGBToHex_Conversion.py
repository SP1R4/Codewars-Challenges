def rgb(r, g, b):
        # helper function
    def help(c):
        if c<0: return 0
        if c>255: return 255
        return c
    
    # make sure that values are within bounds
    r = help(r)
    g = help(g)
    b = help(b)
    
    # convert to hex
    # maintain 2 spaces each
    val = "%02x%02x%02x" % (r, g, b)
    
    # return UpperCase string
    return val.upper()

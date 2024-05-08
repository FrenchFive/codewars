def is_valid_walk(walk):
    #length test 
    if len(walk) == 10:
        north = walk.count("n")
        south = walk.count("s")
        east = walk.count("e")
        west = walk.count("w")
        if north - south == 0 and east - west == 0:
            return(True)
        else:
            return(False)
    else:
        return(False)

walk = ['w','e','w','e','w','e','w','e','w','e','w','e']
print(is_valid_walk(walk))
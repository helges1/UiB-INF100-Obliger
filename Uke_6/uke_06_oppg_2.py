def render_image(grid):
    
    bilde=""
    maks = len(grid[-1])

    for y in range(len(grid[-1])):
        #print(y)

        for x in reversed(range(len(grid))):
            #print(x)

            bilde += grid[x][y]

            if x == 0:
                if y == maks - 1:
                    bilde = bilde 
                else:
                    bilde += '\n'

    return(bilde)
    
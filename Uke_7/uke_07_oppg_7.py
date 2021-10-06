def render_plot(coords):
    xs, ys = zip(*coords)

    x_max = max(xs)
    x_min = min(xs)
    y_max = max(ys)
    y_min = min(ys)

    x_diff = x_max - x_min + 1

    ramme = "#" * (x_diff + 2)
    plot = ""

    for i in reversed(range(y_min, y_max + 1)):
        plot += "#"
        if i in ys:

            for k, j in enumerate(ys):

                if j == i:

                    for n in range(x_min, x_max + 1):

                        if n != xs[k]:
                            plot += " "

                        if n == xs[k]:
                            plot += "*"            

        else:
            plot += " " * (x_diff)
            
        plot += "#" + '\n'

    resultat = ramme + '\n' + plot + ramme 

    return resultat
    

print(render_plot([(2, 3), (-1, 2), (1, -1), (0, 1)]))

print(render_plot([(473, -515)]))

print(render_plot([(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)]))
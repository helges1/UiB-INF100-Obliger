# Med litt hjelp av Christoffer Slettebø
def render_plot(verdi):
    ny_tuple=data_plot(verdi)

    maks_x = max(ny_tuple[0])+1
    min_x = min(ny_tuple[0])
    maks_y = max(ny_tuple[1])
    min_y = min(ny_tuple[1])-1

    tegning = "#"*(maks_x - min_x + 2)+"\n"

    for ys in range(maks_y,min_y,-1):
        tegning += "#"

        for xs in range(min_x,maks_x,1):

            if (xs,ys) in verdi:
                    tegning += "*"

            else:
                    tegning += " "

        tegning +="#"
        tegning +="\n"
    tegning += "#"*(maks_x - min_x + 2)
    return tegning

def data_plot(liste):
    tilListe = list(liste)
    liste1=[]
    liste2=[]

    for x in tilListe:
        a=0

        for verdi in x:
            if a==0:
                liste1.append(verdi)
                a+=1

            else:
                liste2.append(verdi)
                a==0

    plot_render = (liste1,liste2)

    return plot_render

#print(render_plot([(2, 3), (-1, 2), (1, -1), (0, 1)]))

#print(render_plot([(473, -515)]))

#print(render_plot([(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)]))
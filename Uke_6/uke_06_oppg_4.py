#⚠⚠⚠Prøvde meg også på oppgave 4, denne er ikke helt riktig

def render_histogram(liste):
    x = max(liste)
    if all(i <= 0 for i in liste):
        pass
    else:

        histo = ""
        k=0

        
        _liste = [(lambda i: i - 1)(i) for i in liste]
        render_histogram(_liste)

        
        for i in liste:
         
            if i > k:
                histo += '*'
                
                
                
            elif i <= k:
                histo += ' '
                
        visHistogram = histo
        # Virker ikke hvis jeg ikke velger return
        
        print(visHistogram)

        
        

     


#Brukt til testing
print(render_histogram([5, 4, 2, 7, 0, 3, 10]))

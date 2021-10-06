def pigify(ord_):

    if ord_[0] in 'aeiou':
        oversatt = ord_ + "way"

    else:
        n = 0

        for bokstav in ord_:
            if bokstav not in 'aeiou':
                n += 1

            elif bokstav in 'aeiou':
                break

            første_del = ord_[n:]
            siste_del = ord_[:n]
            oversatt = første_del + siste_del + "ay"

    return oversatt
    
# print(pigify("apple"))

def pigify_sentence(setning):
  ulike_ord = setning.split()

  for i, _ord in enumerate(ulike_ord):
    
      if _ord[0] in 'aeiou':
        ulike_ord[i] = ulike_ord[i]+ "way"
        
      else:
          vokal = False
        
          for v, bokstav in enumerate(_ord):
              if bokstav in 'aeiou':
                  vokal = True
                  ulike_ord[i] = _ord[v:] + _ord[:v] + "ay"
                  break

          if(vokal == False):
              ulike_ord[i] = ulike_ord[i]+ "ay"

  oversatt = ' '.join(ulike_ord)
  return oversatt

# print(pigify_sentence("of sitting by her sister on the bank and of having nothing to do"))


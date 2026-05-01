nomes= ["ana", "maria", "vini", "math"]
# ana = maria
# ana = vini
# ana = math
#
# maria = vini
# maria = math
#
# vini = math
# nomes[0] = "ana"
# nomes[1] = "maria"
# nomes[2] = "vini"
# nomes[3] = "math"






for i in range(len(nomes)):
    for j in range(i+1,len(nomes)):
        print(nomes[i], nomes[j])
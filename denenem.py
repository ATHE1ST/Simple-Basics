liste1=['Ankara','İzmir','İstanbul','Adana','Bursa','Kars','Iğdır']
liste2=['Edirne','Aydın']
liste1.extend(liste2)
yer=liste1.index('İstanbul')
liste1.pop(yer)
liste1.sort()
print(liste1)
input()
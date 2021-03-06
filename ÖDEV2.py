class Hayvanlar():

    def __init__(self,ortam="Veri yok..",omurga="Veri yok..",et_ot="Veri yok...",meme="Veri yok..",ağırlık="Veri yok..."):
        self.ağırlık =ağırlık
        self.meme =meme
        self.ortam =ortam
        self.omurga = omurga
        self.et_ot = et_ot
    def __str__(self):
        return "Bu tür {}'\nOrtamı: {}\nOmurga: {}\nEtçil veya Otçul: {}\nAğırlık: {}".format(self.meme,self.ortam,self.omurga,self.et_ot,self.ağırlık)
class Köpekler(Hayvanlar):
    def __init__(self,ortam="Veri yok..",omurga="Veri yok..",et_ot="Veri yok...",meme="Veri yok..",ağırlık="Veri yok...",bacak_sayısı=4):
        self.bacak_sayısı =bacak_sayısı
        self.ağırlık =ağırlık
        self.meme =meme
        self.ortam =ortam
        self.omurga = omurga
        self.et_ot = et_ot
    def __str__(self):
        return "Bu tür {}'dir\nOrtamı: {}\nOmurga: {}\nEtçil veya Otçul: {}\nAğırlık: {}\nBacak sayısı: {}".format(self.meme,self.ortam,self.omurga,self.et_ot,self.ağırlık,self.bacak_sayısı)


hayvanlar= Hayvanlar()
köpekler=Köpekler()
while True:
    cevap=input("Hayvanlar için 1, köpekler için 2 ye basınız...")
    if cevap == "1":
        print(hayvanlar)
    elif cevap == "2":
        print(köpekler)
    else:
        break

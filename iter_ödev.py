class Kareler():
    def __init__(self,maks):
        self.maks = maks
        self.kuvvet=0
        
    def __iter__(self):
        return self

    def __next__(self):
        
        if(self.kuvvet <= self.maks):
            
            sonuç = self.kuvvet ** 2
            self.kuvvet += 1
            return sonuç
        else:
            self.kuvvet = 0
            raise StopIteration
            
kareler = Kareler(13)
for i in kareler:
    print(i)

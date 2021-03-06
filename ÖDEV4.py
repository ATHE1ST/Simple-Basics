def çift_mi(sayı):

    if sayı % 2 == 0:
        return sayı
    else:
        raise ValueError("Hatalı...")
sayı=int(input("Bir sayı giriniz: "))
print(çift_mi(sayı))




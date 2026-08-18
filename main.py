from rules_engine import musteri_getir,sigorta_onerileri_bul
from pricing import prim_hesapla
from policy_issuer import police_olustur


def ana_menu():
    print("=" * 50)
    print("BANKASURANS SUBEMIZE HOS GELDINIZ")
    print("=" * 50)

    tc_kimlik=input("Lutfen musteri TC NO giriniz -->")

    musteri=musteri_getir(tc_kimlik)
    if not musteri:
        print("Bu TC NO ya ait müsteri bulunamadı")
        return
    isim=musteri[1]
    print(f"Musteri bulundu:{isim}")
    print("-" * 50) 
    print("Uygun sigorta teklifleri hesaplaniyor...\n")
    oneriler=sigorta_onerileri_bul(musteri)  
    if not oneriler:
        print("Bu musteriye ait sigorta teklifi bulunmamaktadir")
        return
    teklif_listesi=[]

    for i,sigorta in enumerate(oneriler,1):
        fiyat=prim_hesapla(sigorta,musteri)
        teklif_listesi.append({"ad":sigorta,"fiyat":fiyat})
        print(f"[{i}] {sigorta} - {fiyat:.2f} TL")

    print("-" * 50)

    secim=input("Musteri hangi policeyi onayliyor? (Çıkmak için 0,seçmek için numara girin):")    

    if secim==0:
        print("İşlem iptal edildi,iyi günler!")
        return

    try:
        secim_idx=int(secim)-1
        secilen_teklif=teklif_listesi[secim_idx]

        print("Police kesiliyor,lütfen bekleyiniz...")


        if "DASK" in secilen_teklif["ad"] or "Konut" in secilen_teklif["ad"]:
            teminat=150000.00

        else:
            teminat=500000.00    

        police_olustur(tc_kimlik,secilen_teklif["ad"],secilen_teklif["fiyat"],teminat)
    except(ValueError,IndexError):
        print("HATA:Yanlış bir tuşa bastınız.Lütfen geçerli bir tuş girin.")    


if __name__=="__main__":
    ana_menu()    
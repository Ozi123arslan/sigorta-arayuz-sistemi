def prim_hesapla(sigorta_turu,musteri):

    yas=musteri[2]
    konut_m2=musteri[4]
    bina_yasi=musteri[5]
    arac_degeri=musteri[6]
    hasarsizlik_kademesi=musteri[7]

    if sigorta_turu=="DASK (Zorunlu Deprem Sigortası)":
        taban_fiyat=500
        m2_maliyeti=konut_m2*15
        yas_riski=bina_yasi*50
        toplam_prim=taban_fiyat+m2_maliyeti+yas_riski
        return toplam_prim
    elif sigorta_turu=="Genişletilmiş Kasko":
        temel_risk_primi=arac_degeri*0.05
        indirimli_prim=temel_risk_primi/hasarsizlik_kademesi
        return indirimli_prim
    elif sigorta_turu=="Kredi Hayat Sigortası":
        yas_carpani=85
        toplam_prim=yas*yas_carpani
        return toplam_prim
    elif sigorta_turu=="Bireysel Emeklilik Sistemi (BES) - Gençlik Planı":
        return 1000.0
    elif sigorta_turu=="Konut Paket Sigortası":
        return 2500.0
    else:
        return 1500

if __name__=="__main__":
    from database import init_db
    from rules_engine import musteri_getir,sigorta_onerileri_bul

    aranan_tc="12371979082"  
    musteri=musteri_getir(aranan_tc)

    if musteri:
        print(f"---{musteri[1]} İÇİN HESAPLANAN PRİM HESAPLAMALARİ")


        onerilenler=sigorta_onerileri_bul(musteri)

        for sigorta in onerilenler:
            hesaplanan_fiyat=prim_hesapla(sigorta,musteri)
            print(f"{sigorta}:{hesaplanan_fiyat:.2f}TL") 
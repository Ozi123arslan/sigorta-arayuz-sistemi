import sqlite3

def musteri_getir(tc_kimlik):
    conn=sqlite3.connect("bankasurans.db")
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM musteriler WHERE tc_kimlik=?",(tc_kimlik,))

    musteri=cursor.fetchone()

    conn.close()

    return musteri

def sigorta_onerileri_bul(musteri):

    oneriler= []


    ad_soyad=musteri[1]
    yas=musteri[2]
    kredi_turu=musteri[3]

    if kredi_turu=="KONUT":
        oneriler.append("DASK (Zorunlu Deprem Sigortası)")
        oneriler.append("Konut Paket Sigortası")
        oneriler.append("Kredi Hayat Sigortası")
    elif kredi_turu=="TASIT":
        oneriler.append("Zorunlu Trafik Sigortası") 
        oneriler.append("Genişletilmiş Kasko")
        oneriler.append("Kredi Hayat Sigortası")
    elif kredi_turu=="IHTIYAC":
        oneriler.append("Kredi Hayat Sigortası")
        oneriler.append("Ferdi Kaza Sigortası")
    elif kredi_turu=="YOK":
        if yas<30:
            oneriler.append("Bireysel Emeklilik Sistemi (BES) - Gençlik Planı ") 
        else:
            oneriler.append("Tamamlayıcı Saglık Sigortası (TSS)")
            oneriler.append("Bireysel Emeklilik Sistemi (BES)") 
    return oneriler                 

if __name__=="__main__":
    aranan_tc=""
    bulunan_musteri=musteri_getir(aranan_tc)

    if bulunan_musteri:
        isim=bulunan_musteri[1]
        kredisi=bulunan_musteri[3]
   
        print(f"\n---MÜŞTERIİ BİLGİLERİ---")
        print(f"Müşteri:{isim}")
        print(f"Aktif kredi türü:{kredisi}")

        teklifler=sigorta_onerileri_bul(bulunan_musteri)

        print(f"\n---{isim} İÇİN BULUNAN SİGORTA ÖNERİLERİ---")
        for teklif in teklifler:
            print(f"-{teklif}")
    else:
        print("Bu TC numarasına ait müsteri bulunamadı.")    

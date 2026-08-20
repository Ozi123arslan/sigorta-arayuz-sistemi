import sqlite3
import datetime

def police_olustur(tc_kimlik,sigorta_turu,prim_tutari,teminat_tutari):


    conn=sqlite3.connect("bankasurans.db")
    cursor=conn.cursor()


    bugun=datetime.date.today().strftime("%Y-%m-%d")


    sorgu = """
    INSERT INTO policeler (tc_kimlik,sigorta_turu,tarih,prim_tutari,teminat_tutari)
    VALUES(?,?,?,?,?)
     """
    cursor.execute(sorgu,(tc_kimlik,sigorta_turu,bugun,prim_tutari,teminat_tutari))
    conn.commit()
    conn.close()


    print(f"BAŞARILI✅ {tc_kimlik} TC numarasına sahip müşteriye {sigorta_turu} policesi kesildi")
    print(f"TUTAR:{prim_tutari:.2f} TL | Tarih: {bugun}")


__name__=="__main__"

onaylayan_tc="12371979082"
secilen_sigorta="DASK (Zorunlu Deprem Sigortası)"

onaylanan_tutar=3400.0

koruma_bedeli=150000.0
if __name__=="__main__":
    
    police_olustur(onaylayan_tc,secilen_sigorta,onaylanan_tutar,koruma_bedeli)






    
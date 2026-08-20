import tkinter as tk
from grafik_deneme import grafik_goster
from rules_engine import musteri_getir,sigorta_onerileri_bul
from pricing import prim_hesapla
from policy_issuer import police_olustur
from tkinter import messagebox



pencere=tk.Tk()
pencere.title("BANKASURANS SUBE EKRANI")
pencere.geometry("600x400")
pencere.configure(bg="#f0f0f0")

def sorgula_tiklandi():
    girilen_tc=tc_kutu.get()
   
    musteri=musteri_getir(girilen_tc)

    if not musteri:
        sonuc_etiketi.config(text="HATA:Müşteri Sistemde Bulunamadı!",fg="red")
    else:
        isim=musteri[1]
        sonuc_etiketi.config(text=f"Müşteri:{isim}",fg="green")
        oneriler=sigorta_onerileri_bul(musteri)

        teklif_kutu.delete(0,tk.END)

        if not oneriler:
            sonuc_etiketi.config(text=f"Müşteri:{isim}\nUygun sigorta teklifi bulunamadı.",fg="orange")
        else:
           
            for sigorta in oneriler:
                fiyat=prim_hesapla(sigorta,musteri)

                teklif_kutu.insert(tk.END,f"{sigorta} - {fiyat:.2f} TL")    

def police_kes_tiklandi():
    secili_index=teklif_kutu.curselection()

    if not secili_index:
        messagebox.showwarning("Uyarı","Lütfen önce listeden bir poliçe seçiniz!")
        return
    secili_metin=teklif_kutu.get(secili_index)

    parcalar=secili_metin.split(" - ")
    sigorta_adi=parcalar[0]
    fiyat_metni=parcalar[1]

    fiyat=float(fiyat_metni.replace("TL",""))
    tc=tc_kutu.get()

    if "DASK" in sigorta_adi or "Konut" in sigorta_adi:
        teminat=150000.00
    else:                   
        teminat=500000.00
    police_olustur(tc,sigorta_adi,fiyat,teminat)
    messagebox.showinfo("Başarılı İşlem",f"{sigorta_adi} poliçesi başarıyla oluşturuldu ve sisteme kaydedildi!")    


tc_etiket=tk.Label(pencere, text="Lütfen Müşteri T.C. kimlik Numarasını giriniz:",bg="#f0f0f0",font=("Arial",12,"bold"))
tc_etiket.pack(pady=20)

tc_kutu=tk.Entry(pencere, font=("Arial",14),width=20)
tc_kutu.pack(pady=10)

sorgula_buton=tk.Button(pencere,text="Müşteri Sorgula",command=sorgula_tiklandi,bg="#4CAF50",fg="white",font=("Arial",12,"bold"))
sorgula_buton.pack(pady=10)

grafik_buton=tk.Button(text="3D Piyasa Analizini Göster",command=grafik_goster,bg="#4CAF50",font=("Arial",10,"bold"))
grafik_buton.pack(pady=10)

teklif_kutu=tk.Listbox(pencere,font=("Arial",12),width=45,height=5)
teklif_kutu.pack(pady=10)

police_buton=tk.Button(pencere,text="Seçili Poliçeyi Kes",command=police_kes_tiklandi,bg="#2196F3" ,fg="white",font=("Arial",12,"bold"))
police_buton.pack(pady=10)
                       

sonuc_etiketi=tk.Label(pencere,text="",bg="#f0f0f0",font=("Arial",11),justify="left")
sonuc_etiketi.pack(pady=20)


pencere.mainloop()   


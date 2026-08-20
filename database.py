import sqlite3

def init_db():
    conn=sqlite3.connect("bankasurans.db")

    cursor=conn.cursor()

    print("Veritabanı bağlantısı kuruldu.")

    cursor.execute("""
    CREATE TABLE IF  NOT EXISTS musteriler(
        tc_kimlik TEXT PRIMARY KEY,
        ad_soyad TEXT NOT NULL,
        yas INTEGER NOT NULL,
        aktif_kredi_turu TEXT,
        konut_m2 INTEGER DEFAULT 0,
        bina_yasi INTEGER DEFAULT 0,
        arac_kasko_degeri REAL DEFAULT 0,
        hasarsizlik_kademesi INTEGER DEFAULT 4
        )            
                   """ )

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS policeler(
        police_no TEXT PRIMARY KEY,
        tc_kimlik TEXT NOT NULL,
        sigorta_turu TEXT NOT NULL,
        teminat_tutari REAL NOT NULL,
        prim_tutari REAL NOT NULL,
        taksit_sayisi INTEGER DEFAULT 0,
        tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        durum TEXT DEFAULT 'AKTİF',
        FOREIGN KEY(tc_kimlik) REFERENCES musteriler(tc_kimlik)
    )
    """)

    ornek_musteriler= [
     ("12371979082","Fatma KOCATEPE",37,"KONUT",160,6,0,4),
     ("23451121456","Burcu ESENSOY",29,"TASIT",0,0,600000,3),
     ("98769823412","Mustafa GÜRLER",54,"IHTIYAC",90,18,670000.0,6),
     ("20191765398","Ahmet Murat TAYLAN",24,"YOK",0,0,0,4)
    ]
    
    cursor.executemany("""
    INSERT OR IGNORE INTO musteriler VALUES(?,?,?,?,?,?,?,?)
    """,ornek_musteriler)

    conn.commit()
    conn.close()
    print("Veritabanı hazırlandı ve örnek veriler yüklendi")


if __name__=="__main__":
    init_db()

















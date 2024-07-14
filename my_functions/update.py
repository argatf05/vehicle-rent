from tabulate import tabulate

def validate_model_barang():
    while True:
        model_barang = input("Model Barang (hanya huruf, angka, dan spasi, tanpa simbol): ").strip()
        if all(c.isalnum() or c.isspace() for c in model_barang):
            return model_barang.title()
        else:
            print("Model Barang hanya boleh terdiri dari huruf, angka, dan spasi tanpa simbol.")

def validate_warna():
    while True:
        warna = input("Warna (hanya huruf dan spasi): ").strip()
        if all(c.isalpha() or c.isspace() for c in warna):
            return warna.title()
        else:
            print("Warna hanya boleh terdiri dari huruf dan spasi.")

def update_data(database):
    print("\nUpdate data:")
    
    #Printing database saat ini untuk ditampilkan kepada user
    print(tabulate(database, headers="keys", tablefmt='pretty'))
    
    while True:
        kode_barang = input("\nMasukkan Kode barang yang akan diupdate (misal: Code1, Code2, dll): ").strip().lower()
        
        #Mencari item pada database berdasarkan Kode barang
        item_to_update = None
        for item in database:
            if item["Kode barang"].lower() == kode_barang:
                item_to_update = item
                break
        
        if item_to_update:
            break
        else:
            print(f"Kode barang '{kode_barang}' tidak ditemukan. Silakan coba lagi.")

    while True:
        print("\nPilih kolom yang ingin diupdate:")
        print("1. Jenis Barang")
        print("2. Model Barang")
        print("3. Warna")
        print("4. Transmisi")
        print("5. Harga per hari")
        print("6. Selesai update")
        
        pilihan = input("Masukkan pilihan (1-6): ").strip()
        
        if pilihan == '1':
            #Validasi dan update Jenis barang
            while True:
                jenis_barang = input("Jenis Barang (mobil/sepeda motor): ").strip().lower()
                if jenis_barang in ['mobil', 'sepeda motor']:
                    item_to_update["Jenis Barang"] = jenis_barang.title()
                    break
                else:
                    print("Jenis Barang harus diisi dengan 'mobil' atau 'sepeda motor'.")
        
        elif pilihan == '2':
            #Validasi dan update Model Barang
            while True:
                model_barang = validate_model_barang()
                item_to_update["Model Barang"] = model_barang
                break
        
        elif pilihan == '3':
            #Validasi dan update Warna
            while True:
                warna = validate_warna()
                item_to_update["Warna"] = warna
                break
        
        elif pilihan == '4':
            #Validasi dan update Transmisi
            while True:
                transmisi = input("Transmisi (automatic/manual): ").strip().lower()
                if transmisi in ['automatic', 'manual']:
                    item_to_update["Transmisi"] = transmisi.title()
                    break
                else:
                    print("Transmisi harus diisi dengan 'automatic' atau 'manual'.")
        
        elif pilihan == '5':
            #Validasi dan update Harga per hari
            while True:
                harga_per_hari = input("Harga per hari (hanya angka): ").strip()
                if harga_per_hari.isdigit():
                    item_to_update["Harga per hari"] = int(harga_per_hari)
                    break
                else:
                    print("Harga per hari hanya boleh diisi dengan angka.")
        
        elif pilihan == '6':
            print("\nUpdate selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Masukkan angka antara 1-6.")

    print("\nData berhasil diupdate:")
    print(tabulate([item_to_update], headers="keys", tablefmt='pretty'))

    return database

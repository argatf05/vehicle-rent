import re

def validate_kode_barang(database):
    while True:
        kode_barang = input("Masukkan Kode barang baru (format: CodeX, X adalah integer): ").strip().title()

        #Validasi format Code"X" dengan X adalah integer
        if re.match(r'^Code\d+$', kode_barang):
            #Cek apakah kode_barang sudah ada pada database atau belum
            if any(item["Kode barang"] == kode_barang for item in database):
                print(f"Kode barang '{kode_barang}' sudah ada dalam database. Masukkan Kode barang yang unik.")
            else:
                return kode_barang
        else:
            print("Format Kode barang salah. Harus berupa 'CodeX' di mana X adalah integer.")

def validate_jenis_barang():
    while True:
        jenis_barang = input("Jenis Barang (mobil/sepeda motor): ").strip().lower()
        if jenis_barang in ['mobil', 'sepeda motor']:
            return jenis_barang.title()
        else:
            print("Jenis Barang harus diisi dengan 'mobil' atau 'sepeda motor'.")

def validate_model_barang():
    while True:
        model_barang = input("Model Barang (hanya huruf dan angka, tanpa simbol): ").strip()
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

def validate_transmisi():
    while True:
        transmisi = input("Transmisi (automatic/manual): ").strip().lower()
        if transmisi in ['automatic', 'manual']:
            return transmisi.title()
        else:
            print("Transmisi harus diisi dengan 'automatic' atau 'manual'.")

def validate_harga_per_hari():
    while True:
        harga_per_hari = input("Harga per hari (hanya angka): ").strip()
        if harga_per_hari.isdigit():
            return int(harga_per_hari)
        else:
            print("Harga per hari hanya boleh diisi dengan angka.")

def create_data(database):
    print("\nCreate data:")

    while True:
        new_item = {}

        #Proses penginputan dengan validasi
        new_item["Kode barang"] = validate_kode_barang(database)
        new_item["Jenis Barang"] = validate_jenis_barang()
        new_item["Model Barang"] = validate_model_barang()
        new_item["Warna"] = validate_warna()
        new_item["Transmisi"] = validate_transmisi()
        new_item["Harga per hari"] = validate_harga_per_hari()

        #Penambahan barang baru
        database.append(new_item)
        print(f"\nData dengan Kode barang '{new_item['Kode barang']}' berhasil ditambahkan.")

        #Proses apakah user ingin menambahkan data baru
        while True:
            add_more = input("\nTambahkan data lagi? (y/n): ").strip().lower()
            if add_more == 'y':
                break
            elif add_more == 'n':
                return database
            else:
                print("Pilihan tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")

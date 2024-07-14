from tabulate import tabulate

recycle_bin = []

def view_recycle_bin():
    if recycle_bin:
        print("\nIsi Recycle Bin saat ini:")
        print(tabulate(recycle_bin, headers="keys", tablefmt='pretty'))
    else:
        print("\nRecycle Bin kosong.")

def add_to_recycle_bin(item):
    global recycle_bin
    recycle_bin.append(item)

def restore_from_recycle_bin(database):
    if recycle_bin:
        print("\nPilih data untuk direstore dari Recycle Bin:")
        print(tabulate(recycle_bin, headers="keys", tablefmt='pretty'))
        
        while True:
            kode_barang = input("\nMasukkan Kode barang yang akan direstore: ").strip().capitalize()

            ##Mencari item pada recycle bin berdasarkan Kode barang
            restore_item = None
            for item in recycle_bin:
                if item["Kode barang"] == kode_barang:
                    restore_item = item
                    break
            
            if restore_item:
                database.append(restore_item)
                recycle_bin.remove(restore_item)
                print(f"\nData dengan Kode barang '{kode_barang}' berhasil direstore.")
                break
            else:
                print(f"Kode barang '{kode_barang}' tidak ditemukan di Recycle Bin. Silakan coba lagi.")

    else:
        print("\nRecycle Bin kosong. Tidak ada data untuk direstore.")

    return database

#Mengosongkan recycle bin
def empty_recycle_bin():
    global recycle_bin
    recycle_bin = []
    print("\nRecycle Bin berhasil dikosongkan.")

def recycle_bin_menu(database, recycle_bin):
    while True:
        print('''
        Pilihan menu Recycle Bin:
        1. Lihat isi Recycle Bin
        2. Restore data dari Recycle Bin
        3. Kosongkan Recycle Bin
        4. Kembali
        ''')
        recycle_choice = input("Masukkan pilihan menu Recycle Bin (1-4): ").strip()
        
        if recycle_choice == '1':
            view_recycle_bin()
        elif recycle_choice == '2':
            database = restore_from_recycle_bin(database)
        elif recycle_choice == '3':
            empty_recycle_bin()
        elif recycle_choice == '4':
            break
        else:
            print("Pilihan tidak valid. Masukkan angka antara 1-4.")
    
    return database, recycle_bin

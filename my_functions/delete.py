from tabulate import tabulate
from my_functions.recycle_bin import add_to_recycle_bin

def delete_data(database, recycle_bin):
    print("\nDelete data:")

    #Printing database saat ini untuk ditampilkan kepada user
    print(tabulate(database, headers="keys", tablefmt='pretty'))

    while True:
        kode_barang = input("\nMasukkan Kode barang yang akan dihapus (misal: Code1, Code2, dll): ").strip().lower()

        #Mencari apakah terdapat item di database berdasarkan kode barang
        item_to_delete = None
        for item in database:
            if item["Kode barang"].lower() == kode_barang:
                item_to_delete = item
                break

        if item_to_delete:
            #Menambahkan item ke recycle bin
            add_to_recycle_bin(item_to_delete)
            
            database.remove(item_to_delete)
            print(f"\nData dengan Kode barang '{item_to_delete['Kode barang']}' berhasil dihapus dan dipindahkan ke Recycle Bin.")
            break
        else:
            print(f"Kode barang '{kode_barang}' tidak ditemukan. Silakan coba lagi.")

    print("\nData saat ini di database setelah penghapusan:")
    print(tabulate(database, headers="keys", tablefmt='pretty'))

    return database, recycle_bin

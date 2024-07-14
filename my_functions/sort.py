from tabulate import tabulate

def sort_data(database):
    print("\nSort data:")

    #Printing database saat ini untuk ditampilkan kepada user
    print(tabulate(database, headers="keys", tablefmt='pretty'))

    while True:
        print("\nPilih kolom berdasarkan yang ingin diurutkan:")
        print("1. Kode Barang")
        print("2. Jenis Barang")
        print("3. Model Barang")
        print("4. Warna")
        print("5. Transmisi")
        print("6. Harga per hari")
        print("7. Selesai")

        pilihan = input("Masukkan pilihan (1-7): ").strip()

        if pilihan == '1':
            sorted_database = sort_by_column(database, "Kode barang")
        
        elif pilihan == '2':
            sorted_database = sort_by_column(database, "Jenis Barang")
        
        elif pilihan == '3':
            sorted_database = sort_by_column(database, "Model Barang")
        
        elif pilihan == '4':
            sorted_database = sort_by_column(database, "Warna")
        
        elif pilihan == '5':
            sorted_database = sort_by_column(database, "Transmisi")
        
        elif pilihan == '6':
            sorted_database = sort_by_column(database, "Harga per hari")
        
        elif pilihan == '7':
            print("\nSort data selesai.")
            sorted_database = database
            break
        
        else:
            print("Pilihan tidak valid. Masukkan angka antara 1-7.")
            continue

        print(tabulate(sorted_database, headers="keys", tablefmt='pretty'))

    return sorted_database

def sort_by_column(database, kolom):
    while True:
        urutan = input(f"Pilih urutan untuk kolom '{kolom}':\n"
                      "1. Ascending (A-Z or 0-9)\n"
                      "2. Descending (Z-A or 9-0)\n"
                      "Masukkan pilihan (1 atau 2): ").strip()

        if urutan == '1':
            return sorted(database, key=lambda x: x[kolom])
        elif urutan == '2':
            return sorted(database, key=lambda x: x[kolom], reverse=True)
        else:
            print("Pilihan tidak valid. Masukkan angka 1 atau 2.")

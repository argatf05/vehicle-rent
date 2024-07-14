from tabulate import tabulate
from my_functions.sort import sort_data
from my_functions.validator import validate_name, validate_telephone, validate_email, validate_address
from datetime import datetime, timedelta

rented_vehicles = []

def display_available_vehicles(database):
    updated_database = read_data(database)
    headers = "keys"
    print("\nDaftar Kendaraan yang Tersedia:")
    print(tabulate(updated_database, headers=headers, tablefmt='pretty'))

def read_data(database):
    #Fungsi untuk membaca data dan meng-exclude kendaraan yang sudah disewakan
    if rented_vehicles:
        updated_database = [vehicle for vehicle in database if vehicle["Kode barang"].capitalize() not in [rv["Kode Barang"].capitalize() for rv in rented_vehicles]]
    else:
        updated_database = database[:]
    
    return updated_database

def is_vehicle_available(kode_barang):
    #Fungsi untuk cek apakah kendaraan dengan Kode barang tertentu ada untuk disewakan
    for vehicle in rented_vehicles:
        if vehicle["Kode Barang"].capitalize() == kode_barang:
            return False
    return True

def rent_vehicle(database):
    global rented_vehicles

    print("\nPilih kendaraan yang ingin Anda sewa berdasarkan Kode Barang (case insensitive):")
    kode_barang = input("Masukkan Kode Barang: ").strip().capitalize()

    vehicle = None

    for item in database:
        if item["Kode barang"].capitalize() == kode_barang:
            vehicle = item
            break

    if not vehicle:
        print(f"Tidak ada kendaraan dengan Kode Barang '{kode_barang}' yang tersedia.")
        return None

    if not is_vehicle_available(kode_barang):
        print(f"Kendaraan dengan Kode Barang '{kode_barang}' sudah tidak tersedia untuk disewa.")
        return None

    #Printing kendaraan yang terpilih untuk sewa
    print("\nAnda telah memilih kendaraan:")
    print(tabulate([vehicle], headers="keys", tablefmt='pretty'))

    #Input dan Validasi input user untuk jumlah hari rental
    while True:
        try:
            days = int(input("Masukkan jumlah hari untuk disewa: "))
            if days <= 0:
                print("Jumlah hari harus lebih dari 0.")
            else:
                break
        except ValueError:
            print("Masukkan harus berupa angka.")

    #Input dan Validasi data konsumen
    while True:
        name = input("Nama: ").strip()
        if not validate_name(name):
            print("Nama harus terdiri dari huruf saja dan harus diawali huruf besar.")
        else:
            break

    while True:
        telephone = input("Nomor Telepon: ").strip()
        if not validate_telephone(telephone):
            print("Nomor Telepon harus terdiri dari angka saja dan minimal 10 digit.")
        else:
            break

    while True:
        email = input("Email: ").strip()
        if not validate_email(email):
            print("Format Email tidak valid.")
        else:
            break

    while True:
        address = input("Alamat pengiriman kendaraan: ").strip()
        if not validate_address(address):
            print("Alamat hanya boleh terdiri dari huruf, angka, dan spasi.")
        else:
            break

    #Menghitung total biaya rental
    rental_price_per_day = vehicle["Harga per hari"]
    total_rental_cost = rental_price_per_day * days

    #Mencetak invoice
    print("\nInvoice:")
    print("------------------------------")
    print(f"Nama Kendaraan: {vehicle['Model Barang']}")
    print(f"Kode Barang: {vehicle['Kode barang']}")
    print(f"Harga Sewa per Hari: Rp {rental_price_per_day:,}")
    print(f"Jumlah Hari: {days}")
    print(f"Total Biaya Sewa: Rp {total_rental_cost:,}")
    print("------------------------------")

    #Menghitung ekspektasi tanggal pengembalian
    today = datetime.now()
    return_date = today + timedelta(days=days)
    print(f"Tanggal Harus Kembali: {return_date.strftime('%d %B %Y')}")

    #Pembayaran
    while True:
        try:
            payment_amount = int(input(f"\nMasukkan jumlah uang yang Anda bayarkan (Rp {total_rental_cost:,}): "))
            if payment_amount < total_rental_cost:
                print("Uang yang Anda masukkan kurang dari total biaya sewa.")
            elif payment_amount > total_rental_cost:
                change = payment_amount - total_rental_cost
                print(f"Terima kasih! Uang kembalian Anda: Rp {change:,}")
                break
            else:
                print("Terima kasih! Uang yang Anda masukkan pas.")
                break
        except ValueError:
            print("Masukkan harus berupa angka.")

    #Menambahkan kendaraan yang sudah dirental kedalam list
    rented_vehicles.append({
        "Nama": name,
        "Nomor Telepon": telephone,
        "Email": email,
        "Alamat Pengiriman": address,
        "Kendaraan": vehicle["Model Barang"],
        "Kode Barang": vehicle["Kode barang"],
        "Harga Sewa per Hari": rental_price_per_day,
        "Jumlah Hari": days,
        "Total Biaya Sewa": total_rental_cost,
        "Tanggal Harus Kembali": return_date,
        "Uang Bayar": payment_amount
    })

    return {
        "Nama": name,
        "Nomor Telepon": telephone,
        "Email": email,
        "Alamat Pengiriman": address,
        "Kendaraan": vehicle["Model Barang"],
        "Kode Barang": vehicle["Kode barang"],
        "Harga Sewa per Hari": rental_price_per_day,
        "Jumlah Hari": days,
        "Total Biaya Sewa": total_rental_cost,
        "Tanggal Harus Kembali": return_date,
        "Uang Bayar": payment_amount
    }

def return_vehicle():
    global rented_vehicles

    if not rented_vehicles:
        print("Belum ada kendaraan yang disewa saat ini.")
        return

    print("\nDaftar Kendaraan yang Sedang Disewa:")
    headers = ["Nama", "Nomor Telepon", "Kendaraan", "Kode Barang", "Harga Sewa per Hari", "Jumlah Hari", "Total Biaya Sewa", "Tanggal Harus Kembali"]

    rows = []
    for vehicle in rented_vehicles:
        rows.append([
            vehicle["Nama"], 
            vehicle["Nomor Telepon"], 
            vehicle["Kendaraan"], 
            vehicle["Kode Barang"], 
            vehicle["Harga Sewa per Hari"], 
            vehicle["Jumlah Hari"], 
            vehicle["Total Biaya Sewa"], 
            vehicle["Tanggal Harus Kembali"].strftime('%d %B %Y'),
        ])

    print(tabulate(rows, headers=headers, tablefmt='pretty'))

    #Penginputan kode barang yang ingin dikembalikan
    while True:
        kode_barang = input("\nMasukkan Kode Barang kendaraan yang ingin Anda kembalikan (case insensitive): ").strip().capitalize()

        for vehicle in rented_vehicles:
            if vehicle["Kode Barang"].capitalize() == kode_barang:
                print("\nDetail Kendaraan yang Akan Dikembalikan:")
                print(tabulate([[
                    vehicle["Nama"], 
                    vehicle["Nomor Telepon"], 
                    vehicle["Kendaraan"], 
                    vehicle["Kode Barang"], 
                    vehicle["Harga Sewa per Hari"], 
                    vehicle["Jumlah Hari"], 
                    vehicle["Total Biaya Sewa"], 
                    vehicle["Tanggal Harus Kembali"].strftime('%d %B %Y'), 
                ]], headers=headers, tablefmt='pretty'))

                confirm = input("Apakah Anda yakin ingin mengembalikan kendaraan ini? (y/n): ").lower()
                if confirm == 'y':
                    rented_vehicles.remove(vehicle)
                    print(f"Kendaraan dengan Kode Barang '{kode_barang}' telah dikembalikan.")
                return

        print(f"Tidak ada kendaraan dengan Kode Barang '{kode_barang}' yang sedang disewa.")

def customer_menu(database):
    while True:
        print('''
        Halo, apa yang ingin Anda lakukan hari ini?
            
        1. Tampilkan Pilihan Kendaraan yang Tersedia
        2. Urutkan Pilihan Kendaraan yang Tersedia
        3. Pilih Kendaraan yang Ingin Disewa
        4. Pilih Kendaraan yang Ingin Dikembalikan
        5. Keluar
        ''')

        inputan = input('Masukkan pilihan menu: ')
        if inputan == '1':
            display_available_vehicles(database)
        elif inputan == '2':
            sorted_database = sort_data(database)
            database = sorted_database
            print("Pilihan Kendaraan yang Tersedia telah diurutkan.")
        elif inputan == '3':
            while True:
                rented_vehicle_details = rent_vehicle(database)
                if rented_vehicle_details:
                    print("\nTerima kasih atas transaksi Anda!\n")
                    proceed = input("Apakah Anda ingin menyewa kendaraan lain? (y/n): ").lower()
                    if proceed != 'y':
                        break
        elif inputan == '4':
            return_vehicle()
        elif inputan == '5':
            print("Terima kasih, Anda telah keluar dari menu Customer.")
            break
        else:
            print('Menu yang Anda pilih tidak ada, mohon masukkan menu antara 1-5')
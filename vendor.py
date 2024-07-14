from tabulate import tabulate
from my_functions.create import create_data
from my_functions.update import update_data
from my_functions.delete import delete_data
from my_functions.sort import sort_data
from my_functions.recycle_bin import recycle_bin_menu

def vendor_menu(max_attempts, database, recycle_bin):
    attempts = 0
    while attempts < max_attempts:
        password = input("Masukkan password (atau ketik 'back' untuk kembali): ")
        if password == "12345678":
            while True:
                print('''
                Selamat Bekerja!
                                
                Pilihan menu:
                1. Read Data
                2. Create Data
                3. Update Data
                4. Delete Data
                5. Sort Data
                6. Recycle Bin
                7. Exit
                ''')

                inputan = input('Masukkan pilihan menu: ')
                if inputan == '1':
                    print("\nData saat ini di database:")
                    print(tabulate(database, headers="keys", tablefmt='pretty'))
                elif inputan == '2':
                    database = create_data(database)
                elif inputan == '3':
                    database = update_data(database)
                elif inputan == '4':
                    database, recycle_bin = delete_data(database, recycle_bin)
                elif inputan == '5':
                    database = sort_data(database)
                elif inputan == '6':
                    database, recycle_bin = recycle_bin_menu(database, recycle_bin)
                elif inputan == '7':
                    print("Terima kasih, Anda telah keluar dari menu Vendor.")
                    break
                else:
                    print('Menu yang Anda pilih tidak ada, mohon masukkan menu antara 1-7')
            
            if inputan == '7':
                break
        
        elif password.lower() == 'back':
            break
        
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Password Anda salah. Silakan coba lagi. Anda memiliki {max_attempts - attempts} percobaan lagi.")
            else:
                print(f"Anda telah melebihi batas percobaan. Silakan coba lagi nanti atau coba kembali dengan password yang benar.")

    return database, recycle_bin

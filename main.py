from tabulate import tabulate
from vendor import vendor_menu
from customer import customer_menu
from my_functions.read import read_data 

def main():
    max_attempts = 3
    
    database = read_data()
    
    recycle_bin = []

    while True:
        print('''
        SELAMAT DATANG DI RENTAL MOBIL DAN MOTOR XYZ
                
        Apakah Anda Vendor/Customer?
        1. Vendor
        2. Customer
        3. Exit
        ''')

        parties = input('Masukkan pilihan (1/2/3): ')
        
        if parties == '1':
            database, recycle_bin = vendor_menu(max_attempts, database, recycle_bin)  
        
        elif parties == '2':
            customer_menu(database)
        
        elif parties == '3':
            print("Terima kasih, Anda telah keluar dari program.")
            break
        
        else:
            print('Menu yang Anda pilih tidak ada, mohon masukkan menu antara 1-3')

if __name__ == "__main__":
    main()

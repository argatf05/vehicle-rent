import re

def validate_name(nama):
    #Validasi nama hanya alphabet dan capitalize
    if not nama.isalpha():
        return False
    return True

def validate_telephone(telp):
    #Validasi nomor telp hanya digit dan memiliki minimal 10 digit
    if not telp.isdigit() or len(telp) < 10:
        return False
    return True

def validate_email(email):
    #Validasi email menggunakan regex
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(regex, email):
        return False
    return True

def validate_address(alamat):
    #Validasi alamat address hanya alphabet, digit, dam spasi
    if not alamat.replace(' ', '').isalnum():
        return False
    return True

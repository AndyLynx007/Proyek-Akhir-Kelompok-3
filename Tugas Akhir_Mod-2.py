import os

#Fungsi Menu
def menu():
    print()
    print('''
============================================================================================
     _______. __  .___  ___.      ___       _______       ___      .___  ___.      ___      
    /       ||  | |   \/   |     /   \     |       \     /   \     |   \/   |     /   \     
   |   (----`|  | |  \  /  |    /  ^  \    |  .--.  |   /  ^  \    |  \  /  |    /  ^  \    
    \   \    |  | |  |\/|  |   /  /_\  \   |  |  |  |  /  /_\  \   |  |\/|  |   /  /_\  \   
.----)   |   |  | |  |  |  |  /  _____  \  |  '--'  | /  _____  \  |  |  |  |  /  _____  \  
|_______/    |__| |__|  |__| /__/     \__\ |_______/ /__/     \__\ |__|  |__| /__/     \__\ 
============================================================================================                                                                                            

Selamat datang di Sistem Manajemen Data Mahasiswa (SIMADAMA).
Apa yang ingin anda lakukan saat ini?
1. Tampilkan Data
2. Tambah Data
3. Hapus Data
4. Cari Data
5. Sortir Data
    
9. Keluar''')
    
    choice = input("Masukkan Pilihan anda: ")
    return choice

#Fungsi Baca Data
def read_data():
    if not os.path.exists("data_mahasiswa.txt"):                        #Ada Path Penyimpanan
        return []
    with open("data_mahasiswa.txt", "r") as file:                       #Ada Path Penyimpanan
        data = [line.strip().split(",") for line in file.readlines()]
    return data

# Fungsi Tulis Data
def write_data(data):
    with open("data_mahasiswa.txt", "w") as file:                       #ada path penyimpanan
        for mahasiswa in data:
            file.write(",".join(mahasiswa) + "\n")

#Fungsi Menampilkan Data
def display_data(data):
    if not data:
        print("Tidak ada data mahasiswa.")
    else:
        try:
            print(f"{'No':<5} {'Nama':<20} {'NIM':<10} {'Program Studi':<15}")
            for i, mahasiswa in enumerate(data):
                print(f"{i+1:<5} {mahasiswa[0]:<20} {mahasiswa[1]:<10} {mahasiswa[2]:<15}")
        except:
            print('File anda mungkin rusak')

    b = input("Tekan Enter untuk kembali")
    
# Tambah Data
def add_data():
    Nama = input("Masukkan Nama: ")
    NIM = input("Masukkan NIM: ")
    Prodi = input("Masukkan Prodi: ")

    Mahasiswa = [Nama, NIM , Prodi]
    data = read_data()
    if Mahasiswa not in data:    
        data.append(Mahasiswa)
        write_data(data)
        print('Data berhasil ditambahkan')
    else:
        print("Data sudah ada, Silahkan hapus terlebih dahulu jika ingin diganti.")    


    b = input("Tekan Enter untuk kembali")
    
#Hapus Data
def delete_data():
    Nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
    NIM = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    data = read_data()
    
    for mahasiswa in data:
        if mahasiswa[1] == NIM and mahasiswa[0] == Nama:
            data.remove(mahasiswa)
            write_data(data)
            print("Data berhasil dihapus!")
            b = input("Tekan Enter untuk kembali")
            return
    print("Data tidak ditemukan.")
    b = input("Tekan Enter untuk kembali")

#Pilihan Pencarian Data    
def find_data():
    print('''Cari data mahasiswa berdasarkan:
          1. NIM
          2. Nama''')
    
    choice = input("Masukkan Pilihan: ")
    if choice == '1':
        find_data_nim()
    elif choice == '2':
        find_data_name()

#Cari data (NIM)
def find_data_nim():
    nim = input("Masukkan NIM mahasiswa yang dicari: ").lower()
    data = read_data()
    
    for mahasiswa in data:
        if mahasiswa[1].lower() == nim:
            print(f"Data ditemukan: Nama: {mahasiswa[0]}, NIM: {mahasiswa[1]}, Program Studi: {mahasiswa[2]}")
            b = input("Tekan Enter untuk kembali")
            return
    print("Data tidak ditemukan.")
    b = input("Tekan Enter untuk kembali")

#Cari data (Nama)
def find_data_name():
    nama = input("Masukkan Nama mahasiswa yang dicari: ").lower()
    data = read_data()
    
    for mahasiswa in data:
        if mahasiswa[0].lower() == nama:
            print(f"Data ditemukan: Nama: {mahasiswa[0]}, NIM: {mahasiswa[1]}, Program Studi: {mahasiswa[2]}")
            b = input("Tekan Enter untuk kembali")
            return
    print("Data tidak ditemukan.")
    b = input("Tekan Enter untuk kembali")

#Fungsi Pilihan Sortir
def sort_data():
    print('''Sortir data mahasiswa berdasarkan:
          1. NIM
          2. Nama''')
    
    choice = input("Masukkan Pilihan: ")
    if choice == '1':
        sort_data_nim()
    elif choice == '2':
        sort_data_name()

#Fungsi Sortir Data (NIM)
def sort_data_nim():
    data = read_data()
    if not data:
        print("Tidak ada data yang bisa diurutkan.")
        return
    
    data.sort(key=lambda x: x[1])  
    write_data(data)
    print("Data berhasil diurutkan berdasarkan NIM!")
    display_data(data)

#Fungsi Sortir Data (Nama)
def sort_data_name():
    data = read_data()
    if not data:
        print("Tidak ada data yang bisa diurutkan.")
        return
    
    data.sort(key=lambda x: x[0])  
    write_data(data)
    print("Data berhasil diurutkan berdasarkan Nama!")
    display_data(data)

a = 0
while a != 9:
    a = menu()
    if a == '1':
        data = read_data()
        display_data(data)
    elif a == '2':
        add_data()
    elif a == '3':
        delete_data()
    elif a == '4':
        find_data()
    elif a == '5':
        sort_data()
    elif a == '9':
        print("Terima kasih telah menggunakan program ini")
        print('\n')
        break
    else:
        b = input("Masukkan Pilihan anda dengan benar (Tekan Enter untuk melanjutkan)")

# APLIKASI ANTRIAN ONLINE APOTEK

from collections import deque

class AntrianOnline:
    def __init__(self):
        self.antrian = deque()
        self.antrian_sorted = deque()
        self.list_antrian_panggil = []
        self.id_counter = 1  

    def tambah_ke_antrian(self, nama, alamat):
        data = {'id': self.id_counter, 'nama': nama, 'alamat': alamat}
        self.id_counter += 1  
        self.antrian.append(data)
        self.antrian_sorted = deque(sorted(self.antrian, key=lambda x: x['nama']))
        print(f"ID: {data['id']}, {nama} ({alamat}) ditambahkan ke dalam antrian.")

    def panggil_antrian(self):
        if not self.antrian:
            print("Antrian kosong.")
        else:
            data = self.antrian.popleft()
            self.antrian_sorted.popleft() 
            print(f"ID: {data['id']}, {data['nama']}, silakan masuk!\n")

            # Pilihan obat
            print("List obat :")
            print("1. Parasetamol (obat penurun demam dan pereda nyeri)")
            print("2 Ibuprofen (obat pereda nyeri dan antiinflamasi)")
            print("3. Ciprofloxacin (antibiotik)")
            print("4. Amoxicillin (antibiotik)")
            print("5. Metformin (untuk pengobatan diabetes)")
            print("6. Amlodipine (untuk tekanan darah tinggi)")
            print("7. Omeprazole (obat untuk masalah lambung)")
            print("8. Salbutamol (inhaler untuk asma)")
            print("9. Oralit (larutan elektrolit untuk rehidrasi)")
            print("10. Ranitidine (obat untuk gangguan lambung)\n")

            obat = input("Masukkan obat yang diinginkan: ")
            print(f"{data['nama']}, pesanan obat: {obat}")

            # Tambahkan informasi ke dalam list_antrian_panggil
            self.list_antrian_panggil.append({'id': data['id'], 'nama': data['nama'], 'obat': obat})

    def lihat_list_antrian_panggil(self):
        print("Antrian yang sudah dipanggil beserta obat:")
        for antrian in self.list_antrian_panggil:
            print(f"{antrian['id']}, {antrian['nama']}, {antrian['obat']}")

    def lihat_antrian(self):
        print("Antrian saat ini:", list(self.antrian))

    def sorting_antrian(self):
        # Buat salinan antrian sebelum diurutkan
        sorted_antrian = self.antrian.copy()

        n = len(sorted_antrian)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if sorted_antrian[j]['nama'] > sorted_antrian[j + 1]['nama']:
                    sorted_antrian[j], sorted_antrian[j + 1] = sorted_antrian[j + 1], sorted_antrian[j]

        print("Antrian berhasil diurutkan berdasarkan nama:")
        for item in sorted_antrian:
            print(item['nama'])

    def binary_search_antrian(self, nama):

        sorted_names = sorted([item['nama'] for item in self.antrian])
        index = self.binary_search_rekursif(nama, sorted_names, 0, len(sorted_names) - 1)
        if index != -1:
            print(f"{nama} ditemukan di indeks {index}")
        else:
            print(f"{nama} tidak ditemukan dalam antrian.")

    def binary_search_rekursif(self, target, data, rendah, tinggi):
        if rendah <= tinggi:
            tengah = (rendah + tinggi) // 2
            if data[tengah] == target:
                return tengah
            elif data[tengah] < target:
                return self.binary_search_rekursif(target, data, tengah + 1, tinggi)
            else:
                return self.binary_search_rekursif(target, data, rendah, tengah - 1)
        else:
            return -1

    def tampilkan_menu(self):
        print("\nMenu:")
        print("1. Masukkan Nama ke dalam Antrian")
        print("2. Panggil Nama dalam Antrian")
        print("3. Lihat Antrian")
        print("4. Urutkan Antrian")
        print("5. Cari Nama dalam Antrian")
        print("6. Lihat antrian yang sudah dipanggil")
        print("7. Keluar")


    def proses_menu(self, pilihan):
        try:
            if pilihan == "1":
                nama = input("Masukkan nama: ")
                alamat = input("Masukkan alamat: ")
                if not nama.strip() or not alamat.strip():  
                    raise ValueError("Nama dan alamat tidak boleh kosong, harus diisi.")
                self.tambah_ke_antrian(nama, alamat)
            elif pilihan == "2":
                self.panggil_antrian()
            elif pilihan == "3":
                self.lihat_antrian()
            elif pilihan == "4":
                self.sorting_antrian()
            elif pilihan == "5":
                nama = input("Masukkan nama yang ingin dicari dalam antrian: ")
                self.binary_search_antrian(nama)
            elif pilihan == "6":
                self.lihat_list_antrian_panggil()
            elif pilihan == "7":
                return True
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Terjadi error: {e}")

def main():
    aplikasi_antrian = AntrianOnline()

    while True:
        aplikasi_antrian.tampilkan_menu()
        print("\n================================")
        pilihan = input("Masukkan nomor menu: ")
        print("================================\n")
        
        try:
            aplikasi_antrian.proses_menu(pilihan)
        except Exception as e:
            print(f"Terjadi error: {e}")

        if pilihan == "7":
            break

if __name__ == "__main__":
    main()
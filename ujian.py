class SistemPendataanPerpustakaan:
    def _init_(self):
        self.daftar_buku = []

    def tambahkan_buku(self):
        """Menambahkan buku baru ke dalam daftar."""
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        self.daftar_buku.append({"judul": judul, "penulis": penulis})
        print(f"Buku '{judul}' oleh {penulis} berhasil ditambahkan.\n")

    def cek_daftar_buku(self):
        """Menampilkan daftar buku yang tersedia."""
        print("Daftar Buku:")
        if self.daftar_buku:
            for indeks, buku in enumerate(self.daftar_buku, 1):
                print(f"{indeks}. '{buku['judul']}' oleh {buku['penulis']}")
        else:
            print("Belum ada buku yang terdaftar.")
        print()

    def hapus_buku(self):
        """Menghapus buku berdasarkan nomor dalam daftar."""
        self.cek_daftar_buku()
        if self.daftar_buku:
            try:
                nomor = int(input("Masukkan nomor buku yang ingin dihapus: "))
                if 1 <= nomor <= len(self.daftar_buku):
                    buku_dihapus = self.daftar_buku.pop(nomor - 1)
                    print(f"Buku '{buku_dihapus['judul']}' oleh {buku_dihapus['penulis']}' berhasil dihapus.\n")
                else:
                    print("Nomor tidak valid.\n")
            except ValueError:
                print("Input harus berupa angka.\n")

    def hitung_buku(self):
        """Menghitung jumlah buku yang tersedia."""
        jumlah = len(self.daftar_buku)
        print(f"Jumlah buku yang tersedia: {jumlah}\n")

    def menu(self):
        """Menampilkan menu utama sistem pendataan perpustakaan."""
        while True:
            print("=" * 60)
            print("Selamat Datang di Sistem Pendataan Perpustakaan")
            print("1. Tambahkan Buku Baru")
            print("2. Cek Daftar Buku")
            print("3. Hapus Buku")
            print("4. Hitung Jumlah Buku yang Tersedia")
            print("5. Exit")
            print("=" * 60)

            pilihan = input("Masukkan pilihan menu (1-5): ")
            print()

            if pilihan == "1":
                self.tambahkan_buku()
            elif pilihan == "2":
                self.cek_daftar_buku()
            elif pilihan == "3":
                self.hapus_buku()
            elif pilihan == "4":
                self.hitung_buku()
            elif pilihan == "5":
                print("Keluar dari program. Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.\n")



sistem = SistemPendataanPerpustakaan()
sistem.menu()

class USSDService:
    def _init_(self):
        # Contoh saldo pengguna
        self.user_balance = 50000  # dalam satuan rupiah
        self.accounts = {
            "081234567890": 20000,  # saldo akun penerima
            "089876543210": 30000
        }
        self.bills = {
            "tagihan_001": 15000,
            "tagihan_002": 25000
        }

    def transfer_pulsa(self, phone_number, amount):
        if phone_number not in self.accounts:
            return "Nomor Penerima Tidak Valid"
        if self.user_balance < amount:
            return "Saldo Tidak Cukup"
        
        # Proses transfer
        self.user_balance -= amount
        self.accounts[phone_number] += amount
        return "Transfer Berhasil"

    def cek_saldo(self):
        return f"Saldo Anda: Rp{self.user_balance}"

    def bayar_tagihan(self, bill_id):
        if bill_id not in self.bills:
            return "Tagihan Tidak Ditemukan"
        amount = self.bills[bill_id]
        if self.user_balance < amount:
            return "Saldo Tidak Cukup"
        
        # Proses pembayaran
        self.user_balance -= amount
        return "Pembayaran Berhasil"

    def main_menu(self):
        while True:
            print("\n1. Transfer Pulsa")
            print("2. Cek Saldo")
            print("3. Bayar Tagihan")
            print("4. Keluar")
            
            pilihan = input("Masukkan pilihan Anda: ")
            
            if pilihan == "1":
                nomor_penerima = input("Masukkan nomor penerima: ")
                jumlah_pulsa = int(input("Masukkan jumlah pulsa: "))
                result = self.transfer_pulsa(nomor_penerima, jumlah_pulsa)
                print(result)
            elif pilihan == "2":
                result = self.cek_saldo()
                print(result)
            elif pilihan == "3":
                nomor_tagihan = input("Masukkan nomor tagihan: ")
                result = self.bayar_tagihan(nomor_tagihan)
                print(result)
            elif pilihan == "4":
                print("Terima kasih telah menggunakan layanan ini!")
                break
            else:
                print("Pilihan Tidak Valid, silakan coba lagi.")

# Simulasi penggunaan
service = USSDService()
service.main_menu()